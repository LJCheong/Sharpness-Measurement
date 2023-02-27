import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import msvcrt
import keyboard
import time

# Path to the folder containing the images
folder_path = 'images'

# List of prefixes for the image sets
set_prefixes = []
numSet = int(input('How many sets are there?\n'))

for i in range(numSet):
    set_prefixes.append(f'set{i+1}')
    print(f'set{i+1}')

# List of image file extenstions to search for
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']

# Output file path for the sharpness values
# output_file_path = 'sharpness_output.txt'
output_file = open('sharpness_values.txt', 'w')

# List to hold the standard deviation values for each set
std_values = []

# Loop through each set of images
for set_prefix in set_prefixes:

    # List of image filenames in the set
    set_filenames = [filename for filename in os.listdir(folder_path) if filename.startswith(set_prefix)]

    # Check if the filenames are having correct extensions
    set_filenameExtension = [filename for filename in set_filenames if any(filename.endswith(ext) for ext in image_extensions)]

    # List to hold the sharpness values for the set
    sharpness_values = []

    # Loop through each image in the set and calculate its sharpness
    for filenameExtension in set_filenameExtension:

        # Load the image
        image = cv2.imread(os.path.join(folder_path, filenameExtension))

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculate the Laplacian of the image
        laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()

        # Add the sharpness value to the list for the set
        sharpness_values.append(laplacian)

        # Write the sharpness value to the output file
        output_file.write('{}: {}\n'.format(filenameExtension, laplacian))

    # Calculate the standard deviation of the sharpness values for the set
    sharpness_std = np.std(sharpness_values)
    std_values.append(sharpness_std)

    # Write the standard deviation to the output file
    output_file.write('Standard deviation of {}: {}\n'.format(set_prefix, sharpness_std))

# Close the output file
output_file.close()

# Create a bar chart of the standard deviation values
fig1 = plt.figure()
plt.plot(set_prefixes, std_values)
plt.title('Standard Deviation of Sharpness Values')
plt.xlabel('Set Prefix')
plt.ylabel('Standard Deviation')
plt.show()

plt.close(fig1)

# Wait for a keypress
print('Press any key to exit...')
msvcrt.getch()

# Exit the program
print('Exiting program...')
exit()
