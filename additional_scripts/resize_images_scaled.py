import os
from PIL import Image

# Define the input and output directories
input_directory = 'stimuli/tools2_original_size/'  # Change this to your input directory
output_directory = 'stimuli/tools2'  # Change this to your output directory
resize_percentage = 20  # Change this to the desired percentage

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):  # Add more extensions if needed
        # Open the image
        with Image.open(os.path.join(input_directory, filename)) as img:
            # Calculate the new size based on the percentage
            width, height = img.size
            new_width = int(width * (resize_percentage / 100))
            new_height = int(height * (resize_percentage / 100))

            # Resize the image
            resized_img = img.resize((new_width, new_height))

            # Save the resized image to the output directory
            output_path = os.path.join(output_directory, filename)
            resized_img.save(output_path)
            print(f'Resized and saved: {output_path}')

print('All images resized and saved.')
