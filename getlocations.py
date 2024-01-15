from PIL import Image

def generate_point_file(image_path, output_file):
    # Open the image
    img = Image.open(image_path)

    # Get the dimensions of the image
    width, height = img.size

    # Open the output file for writing
    with open(output_file, 'w') as file:
        # Iterate through each pixel in the image
        for y in range(height):
            for x in range(width):
                # Get the pixel color at the current coordinates
                pixel = img.getpixel((x, y))

                # Check if the pixel is not white (assuming white is (255, 255, 255))
                if pixel != (255, 255, 255):
                    # Write the coordinates to the file
                    file.write(f"{x},{y}\n")

# Example usage
image_path = "aboelhol.png"
output_file = "output.txt"

generate_point_file(image_path, output_file)
