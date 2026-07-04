import cv2
from ultralytics import YOLO

# 1. Load your custom trained model
# Note: Ensure this path correctly points to your weights file
model_path = r" path_to_your_model "
model = YOLO(model_path)

# If Step 1 returned True, uncomment the next line to push processing to the GPU:
# model.to('cuda')

# 2. Define your source 
# Use 0 for a standard USB Webcam. 
# (If using a Raspberry Pi CSI camera ribbon ribbon cable, see the tip below)
source = 0 

print("Starting smoke and fire detection... Press 'q' to quit.")

# 3. Run prediction loop
# 'show=True' opens the GUI window, 'conf=0.5' ignores weak detections below 50%
results = model.predict(source=source, show=True, conf=0.5, imgsz=320)
