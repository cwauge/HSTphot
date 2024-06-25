import numpy as np
from scipy.stats import std
from astropy.io import fits
from astropy.wcs import WCS





class ACS_data():

    def __init__(self,data_array):
        self.data = data_array


