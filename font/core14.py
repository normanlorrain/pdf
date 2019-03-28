# These are the "standard 14 fonts" specified in 5.5 of the spec.
# Wed have the Adobe Font Metrics stored in this package as well.

import os 
from .afm import AFM


AFM_DIR = "Core14_AFMs"

TIMES_ROMAN = 'Times-Roman'
TIMES_ITALIC = 'Times-Italic'
TIMES_BOLD = 'Times-Bold'
TIMES_BOLDITALIC = 'Times-BoldItalic'
HELVETICA = 'Helvetica'
HELVETICA_OBLIQUE = 'Helvetica-Oblique'
HELVETICA_BOLD = 'Helvetica-Bold'
HELVETICA_BOLDOBLIQUE = 'Helvetica-BoldOblique'
COURIER = 'Courier'
COURIER_OBLIQUE = 'Courier-Oblique'
COURIER_BOLD = 'Courier-Bold'
COURIER_BOLDOBLIQUE = 'Courier-BoldOblique'
SYMBOL = 'Symbol'
ZAPFDINGBATS = 'ZapfDingbats'


def loadMetrics(fontName):
    fh = open(os.path.join(os.path.dirname(__file__), AFM_DIR, f'{fontName}.afm'), 'rb')
    afm = AFM(fh)
    return afm

def stringHeight(s,fontName, pt):
    fh = open(os.path.join(os.path.dirname(__file__), AFM_DIR, f'{fontName}.afm'), 'rb')
    afm = AFM(fh)

    _,h = afm.string_width_height(s)

    hInches = h/1000 * pt / 72
    return hInches


def stringWidth(s,fontName, pt):
    fh = open(os.path.join(os.path.dirname(__file__), AFM_DIR, f'{fontName}.afm'), 'rb')
    afm = AFM(fh)
    w,_ = afm.string_width_height(s)
    wInches = w/1000 * pt / 72
    return wInches

def inches(s,fontName, pt):
    fh = open(os.path.join(os.path.dirname(__file__), AFM_DIR, f'{fontName}.afm'), 'rb')
    afm = AFM(fh)
    w,h = afm.string_width_height(s)

    wInches = w/1000 * pt / 72
    hInches = h/1000 * pt / 72
    return (wInches,hInches) 





if __name__ == "__main__":
    
    print(inches('X',HELVETICA, 720))
    print(inches('x',HELVETICA, 720))
    print(inches('I',HELVETICA, 720))
