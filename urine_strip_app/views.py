from django.shortcuts import render
from .models import UrineStrip
import json
from PIL import Image
import extcolors
import os

def upload_strip(request):
    if request.method == 'POST':
        strip_image = request.FILES['strip_image']
        urine_strip = UrineStrip(strip_image=strip_image)
        urine_strip.save()

        # Process the uploaded image and extract color information
        colors = process_image(strip_image)

        # Save the analysis result to the database
        urine_strip.analysis_result = colors
        urine_strip.save()
        # print(urine_strip)

        # Render the template with the analysis results
        return render(request, 'result.html', {'colors': colors})

    return render(request, 'upload.html')

def process_image(image):
    # Use OpenCV to analyze the image and extract RGB values of colors
    # Implement your own image processing logic here
    # This is just a placeholder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    
    input_name = os.path.join(base_dir, 'strips', image.name)

    output_width = 900                   #set the output size
    img = Image.open(input_name)
    wpercent = (output_width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((output_width,hsize), Image.ANTIALIAS)

    #save
    resize_name = 'resize_' + image.name  #the resized image name
    img.save(resize_name) 

    colors_x = extcolors.extract_from_path(resize_name, tolerance = 15, limit = 10)
   
    labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    colors = []
    for i, (rgb_values, _) in enumerate(colors_x[0]):
        color_dict = {
            "color": f"{labels[i]}",
            "rgb": list(rgb_values)
        }
        colors.append(color_dict)
    
    
    

    # colorsz = {label: list(rgb_values) for (rgb_values, _), label in zip(colors_x[0], labels)}
    # cllol=[]
    # # Print the result
    # for label, rgb_values in colorsz.items():
    #     cllol.append(f"'{label}': {rgb_values},")
 

    return json.dumps(colors)
