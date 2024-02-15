

from ultralytics import YOLO
from PIL import Image

# Load a model
model = YOLO('yolov8n-seg.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
image_path = 'Assets/b768aedc20d9c135b355b7cd8e8beff3/_preview.png'
results = model(image_path)  # predict on an image
from torchvision import transforms



# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename='result.jpg')  # save to disk

    for mask in masks.data:
        # Convert PyTorch tensor to PIL Image
        to_pil = transforms.ToPILImage(mode='L')  # 'L' mode for grayscale images
        pil_image = to_pil(mask)

        # Save the PIL Image
        pil_image.save("output_image.png")







