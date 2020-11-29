# source: https://www.youtube.com/watch?v=9nJ0b1PZalY

# To extract text, we should break the video file frame by frame
# which the image can be ocr'd using pytesseract.

from PIL import Image
import pytesseract
'''
import os
import cv2

# creating directory for the frame
if not os.path.exists('image_frames'):
    os.makedirs('image_frames')

# create video path
test_vid = cv2.VideoCapture('sample.mp4')

# start index or count for the frame
index = 0
while test_vid.isOpened():
    ret, frame = test_vid.read()
    if not ret:
        break
# assign a name to the files
    name = './image_frames/frame' + str(index) + '.png'
    print('Extracting frames...' + name)
    cv2.imwrite(name, frame)
    index = index + 1
    cv2.imshow("Frame", frame)     # cv2.waitKey works if clicked on the cv2.imshow window
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

test_vid.release()
cv2.destroyAllWindows()

'''
# using pytesseract to extract text from one image.
demo = Image.open("./image_frames/frame0.png")
text = pytesseract.image_to_string(demo, lang = 'eng')
print(text)
