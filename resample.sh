#!/bin/bash
# resample.sh: resample audio using SoX
# Kyle Gorman <gormanky@ohsu.edu>

set -e

SOX=sox
EXT=wav
SOXCMD="$SOX -G "%s" -b 16 "%s" remix - rate "%d" dither -s"

SAMPLERATES=(4000 8000 10000 11025 12500 15625 16000