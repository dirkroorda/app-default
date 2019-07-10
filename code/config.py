from os.path import dirname, abspath

PROTOCOL = 'http://'
HOST = 'localhost'
PORT = dict(
    kernel=19600,
    web=9600,
)

OPTIONS = ()

ORG = 'yourorg'
REPO = 'yourrepo'
CORPUS = 'Corpus name'
VERSION = '0.1'
RELATIVE = 'tf'

DOI_TEXT = '10.5281/zenodo.nnn'
DOI_URL = 'https://doi.org/10.5281/zenodo.nnn'

DOC_URL = (
    f'https://nbviewer.jupyter.org/github/{ORG}/{REPO}'
    f'/blob/master/docs/transcription.md'
)
DOC_INTRO = ''
CHAR_URL = DOC_URL
CHAR_TEXT = 'How TF features represent text'

FEATURE_URL = DOC_URL

MODULE_SPECS = ()

ZIP = [REPO]

CONDENSE_TYPE = 'paragraph'  # should be the name of section level 3

NONE_VALUES = {None}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {'lex'}

EXAMPLE_SECTION = '<code>book 1:1</code>'
EXAMPLE_SECTION_TEXT = 'book 1:1'

SECTION_SEP1 = ' '
SECTION_SEP2 = ':'

DEFAULT_CLS = 'txtn'
DEFAULT_CLS_ORIG = 'txtp'

FORMAT_CSS = dict(
    full='txtp',
    plain='txtp',
)

CLASS_NAMES = None

FONT_NAME = 'Gentium'
FONT = 'GentiumPlus-R.ttf'
FONTW = 'GentiumPlus-R.woff'

TEXT_FORMATS = {}
TEXT_FORMATS = {
    'layout-orig-full': 'layoutRich',
}


BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False


def deliver():
  return (globals(), dirname(abspath(__file__)))
