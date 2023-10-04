import cv2
import numpy as np

# Load the image
image = cv2.imread('image2.jpg')

# Define the coordinates of the rectangular region you want to turn black
x1, y1, x2, y2 = 0, 0, 1280, 450

# Create a mask with the same dimensions as the image
mask = np.zeros_like(image)

# Set the specified region in the mask to white (1)
mask[y1:y2, x1:x2] = 255

# Apply the mask to the image to make the specified region black
result = cv2.bitwise_and(image, mask)

# Display the edited image
cv2.imshow('Edited Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the edited image
cv2.imwrite('edited_image.jpg', result)
