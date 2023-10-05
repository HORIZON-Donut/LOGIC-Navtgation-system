import cv2
import numpy as np

# Load the RGB image
image = cv2.imread('image2.jpg')  # Replace 'your_image.jpg' with the path to your image file

# Define rectangle coordinates
top_left_1 = (0, 500)  # (x, y) of the top-left corner
bottom_right_1 = (300, 720)  # (x, y) of the bottom-right corner

top_left_2 = (980, 500)  # (x, y) of the top-left corner
bottom_right_2 = (1280, 720)  # (x, y) of the bottom-right corner

# Define the rectangle color (in BGR format)
rectangle_color = (0, 0, 0)  # Black in BGR

# Draw the filled black rectangle on the image
cv2.rectangle(image, top_left_1, bottom_right_1, rectangle_color, thickness=cv2.FILLED)
cv2.rectangle(image, top_left_2, bottom_right_2, rectangle_color, thickness=cv2.FILLED)

# Display the modified image (optional)
cv2.imshow('Image with Filled Black Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
