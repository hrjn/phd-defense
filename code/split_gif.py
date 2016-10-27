
import os
from PIL import Image


def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s-%s.png' % (outFolder, nframes ) , 'png')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True


extractFrames("opera.gif", "opera")
