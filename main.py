import tensorflow as tf
model = tf.keras.models.load_model("attention_model.keras")
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access camera")
        break

    cv2.imshow("Attention Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    


    img = cv2.resize(frame, (224, 224))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img, verbose=0)

    print(prediction)
    class_names = ["Disengaged","Highly Engaged","Moderately Engaged"]

    predicted_class = np.argmax(prediction[0])
    confidence = prediction[0][predicted_class]

    status = class_names[predicted_class]

    print(status, confidence)

cap.release()
cv2.destroyAllWindows()

