import cv2
from PIL import Image

image_path = "face.jpg"
cascade_path = "haarcascade_frontalface_default.xml"
glasses_path = "glasses.png"

face_cascade = cv2.CascadeClassifier(cascade_path)

img_cv = cv2.imread(image_path)
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

img = Image.open(image_path).convert("RGBA")
glasses = Image.open(glasses_path).convert("RGBA")

for (x, y, w, h) in faces:

    g = glasses.resize((w, int(h/3)))

    img.paste(g, (x, int(y + h/4)), g)

img.save("result_task1.png")

res = cv2.imread("result_task1.png")
cv2.imshow("Result", res)
cv2.waitKey()
