#!/bin/bash
# resample.sh: resample audio using SoX
# Kyle Gorman <gormanky@ohsu.edu>

set -e

SOX=sox
EXT=wav
SOXCMD="$SOX -G "%s" -b 16 "%s" remix - rate "%d" dither -s"

SAMPLERATES=(4000 8000 10000 11025 12500 15625 16000 20000 25000
             31250 40000 50000 62500 78125 80000 100000 125000
             156250 200000)

usage() { 
    echo "Usage: $0 [-s SAMPLERATE] [-r SOURCEDIR] [-w SINKDIR]" >&2
}

fail() {
    usage
    echo "$*" >&2
    echo "Aborting." >&2
    exit 1
}

# check for presence of SoX
command -v $SOX >/dev/null 2>&1 || fail "$SOX not found."

# parse args
while getopts "s:r:w:" OPT; do
    case $OPT in
        s)
            S=$OPTARG
            ;;
        r)
            R=$OPTARG
            ;;
        w)
            W=$OPTARG
            ;;
        \?)
            fail "Invalid option."
            ;;
        :)
            fail "Option '-$OPT' requires an argument."
    esac
done

# check samplerate validity
[ -n "$S"