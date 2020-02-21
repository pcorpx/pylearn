import unicodedata
import string

def shave_marks(txt):
    """ Remove marks """
    norm_txt = unicodedata.normalize('NFD', txt)
    print(norm_txt)


shave_marks('1/2 Vob')