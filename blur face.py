import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('20211130_160833.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Iterate over each detected face
for (x, y, w, h) in faces:
    # Extract the region of interest (the face)
    roi = image[y:y+h, x:x+w]
    
    # Blur the face using a median blur
    roi = cv2.medianBlur(roi, 95)
    
    # Replace the original face with the blurred face
    image[y:y+h, x:x+w] = roi

cv2.imwrite('blurred_image.jpg', image)