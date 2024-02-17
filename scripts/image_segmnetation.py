from ultralytics import YOLO
from PIL import Image

# Load a model
model = YOLO("yolov8n-seg.pt")  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
image_path = "../log.jpeg"
results = model(image_path)  # predict on an image
from torchvision import transforms

model = YOLO("yolov8n-seg.pt")

image_path = "Assets/0a22f881b77f00220f2034c21a18b854/end-bg.jpg"
results = model(image_path)


for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    result.show()  # display to screen
    result.save(filename="log.png")  # save to disk

    for i, mask in enumerate(masks.data):
        # Convert PyTorch tensor to PIL Image
        to_pil = transforms.ToPILImage(mode="L")  # 'L' mode for grayscale images
        pil_image = to_pil(mask)

        # Save the PIL Image
        pil_image.save(f"output_image_{i}.png")
