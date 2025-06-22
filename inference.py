from ultralytics import YOLO

model = YOLO("runs/detect/train4/weights/best.pt")
results = model("dataset/valid/images/zidane.jpg", conf=0.1)
# results[0].show(filename="output.jpg")  # Display
results[0].save(filename="output.jpg")  # Save result
