"""
unittest
"""
import unittest
import numpy as np

from examples import (ex_camera_gaussian_noise, ex_camera_stripes,
                      ex_camera_curtains)


class TestVSNR(unittest.TestCase):
    """
    Test VSNR algorithm
    """

    def test_ex_camera_gaussian_noise(self):
        """ Test VSNR algorithm on guassian noise removal """

        img_corr = ex_camera_gaussian_noise()

        self.assertAlmostEqual(np.sum(img_corr), 133416.55485879257)

    def test_ex_camera_stripes(self):
        """ Test VSNR algorithm on stripes removal """

        img_corr = ex_camera_stripes()

        self.assertAlmostEqual(np.sum(img_corr), 132647.76312657446)

    def test_ex_camera_curtains(self):
        """ Test VSNR algorithm on curtains removal """

        img_corr = ex_camera_curtains()

        self.assertAlmostEqual(np.sum(img_corr), 121879.85710567946)
