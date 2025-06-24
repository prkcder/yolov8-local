from ultralytics import YOLO
import yaml

# model = YOLO("runs/detect/train5/weights/best.pt")

model = YOLO("runs/detect/train4/weights/best.pt")
results = model("dataset/train/images/bus.jpg", conf=0.25)
# results = model("test/images/car.jpg", conf=0.25)
# results[0].show(filename="output.jpg")  # Display

# results[0].print()

results[0].save(filename="output.jpg")  # Save result
# annotated_frame = results[0].plot()
# cv2.imwrite("output.jpg", annotated_frame)


# Manually apply the correct class name
# model.model.names = {0: 'License_Plate'}


# Run inference with lower confidence just in case
# results = model("train/images/00ca4b949dd426f8_jpg.rf.f45f29757aafd545519ef701b6a9d225.jpg", conf=0.1)

# Save annotated output
# for r in results:
#     r.save(filename="output.jpg")