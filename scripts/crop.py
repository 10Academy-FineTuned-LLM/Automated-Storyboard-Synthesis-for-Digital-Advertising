import cv2

# Assuming you have the bounding box coordinates (x, y, width, height) from YOLO
x, y, width, height = 10, 300, 200, 300  # Example coordinates

# Load the original image
image = cv2.imread('bus.jpg')

# Crop the image based on the bounding box
cropped_image = image[y:y+height, x:x+width]

# Save or use the cropped image for further processing
cv2.imwrite('cropped_image.jpg', cropped_image)
