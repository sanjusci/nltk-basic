__author__ = "Sanju Sci"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019"

import pandas as pd


class Helper(object):

    def __init__(self, filename, *args, **kwargs):
        self.filename = filename

    def read(self):
        return pd.read_csv(self.filename)  # doctest: +SKIP

