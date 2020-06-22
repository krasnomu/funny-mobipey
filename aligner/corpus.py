
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
Corpus utilities
"""


import os
import logging

from re import match
from glob import glob
from shutil import rmtree
from tempfile import mkdtemp
from subprocess import check_call

from .wavfile import WavFile
from .prondict import PronDict
from .utilities import splitname, mkdir_p, opts2cfg, \
                       MISSING, OOV, SIL, SP, TEMP


# regexp for inspecting phones
VALID_PHONE = r"^[^\d\s]+[0-9]?$"


class Corpus(object):

    """
    Class representing directory of training data; once constructed, it
    is ready for training or aligning.
    """

    def __init__(self, dirname, opts):
        # temporary directories for stashing the data
        tmpdir = os.environ["TMPDIR"] if "TMPDIR" in os.environ else None
        self.tmpdir = mkdtemp(dir=tmpdir)
        self.auddir = os.path.join(self.tmpdir, "audio")
        mkdir_p(self.auddir)
        self.labdir = os.path.join(self.tmpdir, "label")
        mkdir_p(self.labdir)
        # samplerate
        self.samplerate = opts["samplerate"]
        # phoneset
        self.phoneset = frozenset(opts["phoneset"])
        for phone in self.phoneset:
            if not match(VALID_PHONE, phone):
                logging.error("Phone '{}': not /{}/.".format(phone,
                                                      VALID_PHONE))
                exit(1)
        # dictionaries
        self.dictionary = []
        if "dictionary" in opts and opts["dictionary"]:
            assert type(opts["dictionary"]) is list
            self.dictionary.extend(opts["dictionary"])
        self.thedict = PronDict(self.phoneset)
        for dic in self.dictionary:
            self.thedict.add(dic)
        #self.thedict[SIL] = [SIL]