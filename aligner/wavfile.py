# Copyright (c) 2011-2014 Kyle Gorman and Michael Wagner
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Utilities for audio resampling (etc.)
"""

import wave

from numpy import asarray
from scipy.io import wavfile
from scipy.signal import resample


class WavFile(object):

    """
    Class representing a mono wav file
    """

    def __init__(self, signal, Fs):
        self.signal = asarray(signal)
        self.Fs = Fs

    @staticmethod
    def samplerate(filename):
        """
        Get samplerate without reading the entire wav file into memory
        """
        with wave.open(filename, "r") as source:
            return source.getframerate()

    @classmethod
    def from_file(cls, filename):
        (Fs, signal) = wavfile.read(filename)
        if signal.ndim > 1:
            raise ValueError("Expected mono audio," +
                             " but '{}'".format(filename) +
                             " has {} channels.".format(signal.ndim))
        return cls(signal, Fs)

    def __repr__(self):
        return "{}(signal={!r}, Fs={!r})".format(self.__class__