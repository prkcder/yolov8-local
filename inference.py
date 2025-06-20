from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
results = model("dataset/test/images/sample.jpg")
results[0].show()
results[0].save(filename="output.jpg")