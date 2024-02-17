

from ultralytics import YOLO
from PIL import Image
from torchvision import transforms

model = YOLO('yolov8n-seg.pt')  

image_path = 'Assets/0a22f881b77f00220f2034c21a18b854/end-bg.jpg'
results = model(image_path) 


for result in results:
    boxes = result.boxes  
    masks = result.masks  
    keypoints = result.keypoints 
    probs = result.probs 
    result.show() 
    result.save(filename='result.jpg') 
    for i, mask in enumerate(masks.data):
        to_pil = transforms.ToPILImage(mode='L')  
        pil_image = to_pil(mask)
        pil_image.save(f"output_image.png")







