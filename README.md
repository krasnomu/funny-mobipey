
# Prosodylab-Aligner, v. 1.1

Scripts for alignment of laboratory speech production data

* Kyle Gorman <gormanky@ohsu.edu>
* Michael Wagner <chael@mcgill.ca>

## Funding

* FQRSC Nouvelle Chercheur NP-132516
* SSHRC Canada Research Chair 218503
* SSHRC Digging Into Data Challenge Grant 869-2009-0004

## License

	The MIT License
	
	Copyright (c) 2011-2016 Kyle Gorman and Michael Wagner

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation
    files (the “Software”), to deal in the Software without
    restriction, including without limitation the rights to use,
    copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following
    conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
    HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    OTHER DEALINGS IN THE SOFTWARE.

## Citation

Please you use this tool; we would appreciate if you cited the following paper:

Gorman, Kyle, Jonathan Howell and Michael Wagner. 2011. Prosodylab-Aligner: A Tool for Forced Alignment of Laboratory Speech. Canadian Acoustics. 39.3. 192–193.

## Usage

    USAGE: python3 -m aligner [OPTIONS]

    Option              Function
    
    -c config_file      Specify a configuration file to use     [default: en.yaml]

    -d dictionary       Specify a dictionary file               
                        (NB: available only with -t (See Input Group))

    -h                  Display this message

    -s samplerate (Hz)  Samplerate for models                   [default: SAMPLERATE]
                        (NB: available only with -t)

    -e                  Number of epochs in training per round  [default: EPOCHS]
                        (NB: available only with -t (See Input Group))

    -v                  Verbose output

    -V                  More verbose output

    Input Group:        Only one of the following arguments may be selected

    -r                  Read in serialized acoustic model

    -t training_data/   Perform model training 

    Output Group:       Only one of the following arguments may be selected

    -a                  Directory of data to be aligned

    -w                  Location to write serialized model

## FAQ

### What is forced alignment?

Forced alignment can be thought of as the process of finding the times at which individual sounds and words appear in an audio recording under the constraint that words in the recording follow the same order as they appear in the transcript. This is accomplished much in the same way as traditional speech recognition, but the problem is somewhat easier given the constraints on the "language model" imposed by the transcript.

### What is forced alignment good for?

The primary use of forced alignment is to eliminate the need for human annotation of time-boundaries for acoustic events of interest. Perhaps you are interested in sound change: forced alignment can be used to locate individual vowels in a sociolinguistic interview for formant measurement. Perhaps you are interested in laboratory speech production: forced alignment can be used to locate the target word for pitch measurement.

### Can I use Prosodylab-Aligner for languages other than English?

Yes! If you have a few hours of high quality speech and associated word-level transcripts, Prosodylab-Aligner can induce a new acoustic model, then compute the best alignments for said data according to the acoustic model.

### What are the limitations of forced alignment?

Forced alignment works well for audio from speakers of similar dialects with little background noise. Aligning data with considerable dialect variation, or to speech embedded in noise or music, is currently state of the art.

### How can I improve alignment quality?

You can train your own acoustic models, using as much training data as possible, or try to reduce the noise in your test data before aligning.

### How does Prosodylab-Aligner differ from HTK?

The [Hidden Markov Model Toolkit](http://htk.eng.cam.ac.uk) (HTK) is a set of programs for speech recognition and forced alignment. The [HTK book](http://htk.eng.cam.ac.uk/docs/docs.shtml) describes how to train acoustic models and perform forced alignment. However, the procedure is rather complex and the error messages are cryptic. Prosodylab-Aligner essentially automates the HTK forced alignment workflow.

### How does Prosodylab-Aligner differ from the Penn Forced Aligner?

The [Penn Forced Aligner](http://www.ling.upenn.edu/phonetics/p2fa/) (P2FA) provides forced alignment for American English using an acoustic model derived from audio of US Supreme Court oral arguments. Prosodylab-Aligner has a number of additional capabilities, most importantly acoustic model training, and it is possible in theory to use Prosodylab-Aligner to simulate P2FA.

## Installations instructions for Mac Users

NB: when you are instructed to type in a command, do not type the '$' symbol; it just indicates the start of the prompt.

NB: most of these commands will produce significant text output. You can safely ignore it unless it explicitly is marked as an 'error'.

### Install XCode

XCode is a free application that contains of all the tools you need to compile most software on Mac OS X. You can get it from the Mac App Store) or you can start the download from the Terminal. To do the latter, launch the application 'Terminal.app', then type the following at the prompt, then hit return:

    $ xcode-select --install
Note that this is a large download and will take a while. Start it now! An alternative option that is somewhat smaller is Command Line Tools for Xcode.

### Install HTK (Hidden Markov ToolKit)

HTK is the "backend" that powers the aligner. It is available only as uncompiled code. First, go to the HTK website and register. Then click on 'Download' on the left panel, and then click on 'HTK source code (tar+gzip archive)' under 'Linux/Unix downloads'.

Once this is downloaded, you may have to unpack the "tarball". Launch the application 'Terminal.app' (if you haven't already), and then navigate to your downloads directory (cd ~/Downloads will probably work). Then unpack the tarball like so:

    $ tar -xvzf HTK-3.4.1.tar.gz

Some browsers automatically unpack compressed files that they download. If you get an error when you execute the above command, try the following instead:

    $ tar -xvf HTK-3.4.1.tar

Once you extract the application, navigate into the resulting directory:

    $ cd htk

Once this is complete, the next step is to compile HTK. Execute the following commands inside the htk directory:

    $ export CPPFLAGS=-UPHNALG
    $ ./configure --disable-hlmtools --disable-hslab
    $ make clean    # necessary if you're not starting from scratch
    $ make -j4 all
    $ sudo make -j4 install

(This will take a few minutes.)

At the last step, you may be asked to provide your system password; do so and then hit return. Note that your password will not echo (i.e., no '*' will be produced when you type).

### Install Homebrew

Homebrew is a command-line application for installing software on your Macintosh. It is the easiest way to get the remaining dependencies to run the aligner. To install Homebrew, launch the application 'Terminal.app' (if you haven't already) and type the following:

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

and then follow along with the instructions that are displayed in the terminal window. Once again, you may need to enter your system password, and once again, your password will not echo.

### Install Python 3

Homebrew makes it easy to install the newest version of Python programming language that powers the aligner. To install it, launch the application 'Terminal.app' (if you haven't already) and type the following:

    $ brew install python3

(This will take a few minutes.)

### Install SoX

SoX is the "Swiss Army knife of sound processing programs", and can be used to do fast batch of your audio files (though it is possible to run the aligner without using SoX). Once again, Homebrew makes it easy to install SoX. Launch the application 'Terminal.app' (if you haven't already) and type the following:

    $ brew install sox

(This may take a few minutes.)

### Install the actual aligner

Prosodylab-Aligner lives on GitHub, a repository for open-source software. You may want to create an account there, and perhaps install 'GitHub.app', which makes it easier to interact with GitHub. But for the purposes of installing the aligner, all you need is the git command-line tool, which is part of Xcode (and so should already be installed). Launch the application 'Terminal.app' (if you haven't already) and type the following:
