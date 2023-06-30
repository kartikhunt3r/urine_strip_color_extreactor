color_x = ([((186, 184, 185), 3886908), ((182, 165, 139), 275966), ((54, 50, 51), 120184), ((142, 121, 102), 105924), ((173, 153, 82), 79350), ((124, 160, 148), 63684), ((58, 90, 89), 37510), ((147, 143, 144), 18707), ((222, 207, 186), 15716), ((161, 120, 40), 8773)], 4631400)

labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

colors = {label: list(rgb_values) for (rgb_values, _), label in zip(color_x[0], labels)}

# Print the result
for label, rgb_values in colors.items():
    print(f"'{label}': {rgb_values},")
