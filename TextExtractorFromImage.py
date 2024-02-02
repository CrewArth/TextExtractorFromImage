#Import Libraries
import cv2
import easyocr
import matplotlib.pyplot as plt

#Read Image
img = cv2.imread('TextOCR1.jpg')


#Instance of Text Detector
reader = easyocr.Reader(['en'], gpu=True)

#Read Text from Image
text_from_image = reader.readtext(img)


#Plot it for Result
for text in text_from_image:
    print(text)
    bbox, img_text, score = text

    score = score * 100
    if score > 90:
        cv2.rectangle(img, bbox[0], bbox[2], (0,0,0), 2)
        cv2.putText(img, img_text, bbox[0], cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0,255,0), 2)
    
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()