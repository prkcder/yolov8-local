from ultralytics import YOLO

model = YOLO("runs/detect/train4/weights/best.pt")
results = model("test/images/car.jpg")
# results[0].show(filename="output.jpg")  # Display
results[0].save(filename="output.jpg")  # Save result
