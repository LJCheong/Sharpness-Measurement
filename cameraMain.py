import cv2
import time
import os
import msvcrt
import matplotlib.pyplot as plt

# Connect to capture device
print('Initializing camera')
cap = cv2.VideoCapture(0)

# Create a folder to store the images
print('Image folder created')
if not os.path.exists('images'):
    os.makedirs('images')

# Input the set number of the run
runCount = int(input('Input the set number for this run\n'))

# Input the number of images to be acquired
imageCount = int(input('How much image would you like to collect?\n'))

print(f'Collecting {imageCount} images with 1 second interval')

for i in range(imageCount):
    # get the current time
    timestamp = time.time()

    # Get a frame from the capture device
    ret, frame = cap.read()
    # print(ret)
    # print(frame)

    cv2.imshow('Webcam', frame)
    # plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # save the image with an incremental filename
    filename = f'images/set{runCount}_{i:03d}.jpg'
    cv2.imwrite(filename, frame)
    print(f'image num {i} saved')

    # wait for 1 second before capturing the next image
    time.sleep(1)

# Closes the frame
cv2.destroyAllWindows()

print('Image acquisition done')

# release the camera
cap.release()

# Wait for a keypress
print('Press any key to exit...')
msvcrt.getch()

# Exit the program
print('Exiting program...')
exit()