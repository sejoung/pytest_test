import cv2
import numpy as np


def test_opencv():
    img = cv2.imread("data/Lenna.png")
    img.shape  # (512, 512, 3)
    img = cv2.resize(img, (256, 256))
    img = img[:100, :100]  # crop image
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    img = cv2.filter2D(img, -1, kernel)
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite("data/Lenna_modified.png", img)
