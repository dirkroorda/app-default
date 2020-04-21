from os.path import dirname, abspath

API_VERSION = 1

PROTOCOL = "http://"
HOST = "localhost"
PORT = dict(kernel=19600, web=9600)

ORG = "yourorg"
REPO = "yourrepo"
CORPUS = "Corpus name"
VERSION = "0.1"
RELATIVE = "tf"

DOI_TEXT = "10.5281/zenodo.nnn"
DOI_URL = "https://doi.org/10.5281/zenodo.nnn"

DOC_URL = (
    f"https://nbviewer.jupyter.org/github/{ORG}/{REPO}"
    f"/blob/master/docs/transcription.md"
)
DOC_INTRO = ""
CHAR_URL = DOC_URL
CHAR_TEXT = "How TF features represent text"

FEATURE_URL = DOC_URL

MODULE_SPECS = ()

ZIP = [REPO]

BASE_TYPE = "word"
CONDENSE_TYPE = "paragraph"  # should be the name of section level 3

NONE_VALUES = {None}

STANDARD_FEATURES = None  # meaning all loadable features

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {"lex"}

EXAMPLE_SECTION = "<code>book 1:1</code>"
EXAMPLE_SECTION_TEXT = "book 1:1"

SECTION_SEP1 = " "
SECTION_SEP2 = ":"

WRITING = ""
WRITING_DIR = "ltr"

FONT_NAME = "Gentium"
FONT = "GentiumPlus-R.ttf"
FONTW = "GentiumPlus-R.woff"

TEXT_FORMATS = {}
TEXT_FORMATS = {
    "layout-orig-full": "layoutRich",
}

BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False

VERSE_TYPES = None

LEX = "lex"

TRANSFORM = None

CHILD_TYPE = dict(book="chapter", chapter="sentence", sentence="word", line="word")

SUPER_TYPE = None

TYPE_DISPLAY = dict(
    book=dict(
        template="{title}",
        bareFeatures="author",
        features="",
        level=3, flow="col", wrap=False, stretch=False,
    ),
    chapter=dict(
        template="{number}",
        bareFeatures="",
        features="",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    sentence=dict(
        template="{number}",
        bareFeatures="",
        features="",
        level=2, flow="col", wrap=False, strectch=True,
    ),
    line=dict(
        template="{number}",
        bareFeatures="",
        features="terminator",
        level=1, flow="row", wrap=True, strectch=True,
    ),
    word=dict(
        template=True,
        bareFeatures="",
        features="gap",
        level=0, flow="col", wrap=False, strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
