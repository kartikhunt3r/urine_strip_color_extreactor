# Urine Strip Analyzer

This project is a web application that allows users to upload an image of a urine strip and identify the colors on the strip. It provides color analysis by extracting the RGB values of the colors on the strip.

## Features

- Upload an image of a urine strip and analyze its colors.
- Extract the RGB values of the colors on the strip.
- Display the color analysis results on the web interface.

## Technologies Used

- Backend: Django
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Image Processing: OpenCV
- Python Libraries: PIL, extcolors

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/urine-strip-analyzer.git
   ```

2. Change to the project directory:

   ```bash
   cd urine-strip-analyzer
   ```

3. Install the required Python modules using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Access the web application in your browser at `http://127.0.0.1:8000/`.

## Usage

1. In your web browser, navigate to `http://127.0.0.1:8000/`.
2. Click on the "Upload" button.
3. Choose an image of a urine strip from your local machine and click "Submit".
4. The application will process the image and display the color analysis results on the webpage.
