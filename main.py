import cv2
import imutils
# initializing the HOG person
# detector
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeolpeDetector())
path=r'C:\Users\'