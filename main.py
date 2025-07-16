import cv2
import time
import os

# ✅ Your desired folder
save_directory = r"E:\Machine-Learning-Projects\Smile Selfie Capture Project\Selfies Clicked"

# ✅ Create folder if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

video = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("dataset/haarcascade_smile.xml")

cnt = 1
last_smile_time = 0
show_text = False
text_timer = 0

while True:
    success, img = video.read()
    if not success:
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = grayImg[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        smiles = smileCascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=30)

        if len(smiles) > 0 and (time.time() - last_smile_time) > 3:
            # ✅ Build file path dynamically
            save_path = os.path.join(save_directory, f"selfie_{cnt}.jpg")
            cv2.imwrite(save_path, img)
            print(f"Clicked Selfie! Saved at: {save_path}")
            last_smile_time = time.time()
            cnt += 1
            show_text = True
            text_timer = time.time()
            break

    # ✅ Text overlays
    if show_text and (time.time() - text_timer) < 2:
        cv2.putText(img, "Clicked Selfie!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    else:
        show_text = False

    cv2.putText(img, "Press Q to Quit", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.imshow('Smile Selfie Camera', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
