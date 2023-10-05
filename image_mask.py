import cv2
import numpy as np

# Load the RGB image
image = cv2.imread('image2.jpg')  # Replace 'your_image.jpg' with the path to your image file

# Define the vertices of the trapezoid as a list of points
trapezoid_vertices = np.array([[150, 100], [300, 100], [400, 300], [100, 300]], np.int32)
trapezoid_vertices = trapezoid_vertices.reshape((-1, 1, 2))

# Define the trapezoid color (in BGR format)
trapezoid_color = (0, 0, 255)  # Red in BGR

# Draw the filled trapezoid on the image
cv2.fillPoly(image, [trapezoid_vertices], trapezoid_color)

# Display the modified image (optional)
cv2.imshow('Image with Trapezoid', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
