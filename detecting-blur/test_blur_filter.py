import unittest
import cv2
from blur_filter import blur_laplacian 

class testBlurFilter(unittest.TestCase):
    def test_blur(self):
        self.addTypeEqualityFunc(numpy.ndarray)