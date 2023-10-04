import cv2
import numpy as np

# Load the RGB image
image = cv2.imread('image2.jpg')  # Replace 'your_image.jpg' with the path to your image file

# Define rectangle coordinates
top_left = (400, 500)  # (x, y) of the top-left corner
bottom_right = (880, 720)  # (x, y) of the bottom-right corner

# Define the rectangle color (in BGR format)
rectangle_color = (0, 0, 0)  # Black in BGR

# Draw the filled black rectangle on the image
cv2.rectangle(image, top_left, bottom_right, rectangle_color, thickness=cv2.FILLED)

# Display the modified image (optional)
cv2.imshow('Image with Filled Black Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
