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

EXAMPLE_SECTION = "<code>book 1:1</code>"
EXAMPLE_SECTION_TEXT = "book 1:1"

DATA_DISPLAY = dict(
    noneValues={None},
    sectionSep1=" ",
    sectionSep2=":",
    writing="",
    writingDir="ltr",
    fontName="Gentium",
    font="GentiumPlus-R.ttf",
    fontw="GentiumPlus-R.woff",
    textFormats={"layout-orig-full": "layoutRich"},
    browseNavLevel=2,
    browseContentPretty=False,
)

TYPE_DISPLAY = dict(
    book=dict(
        template="{title}",
        featuresBare="author",
        children="chapter",
        level=3, flow="col", wrap=False, stretch=False,
    ),
    chapter=dict(
        template="{number}",
        children="sentence",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    sentence=dict(
        template="{number}",
        children="word",
        condense=True,
        level=2, flow="col", wrap=False, strectch=True,
    ),
    line=dict(
        template="{number}",
        features="terminator",
        children="word",
        level=1, flow="row", wrap=True, strectch=True,
    ),
    lex=dict(
        template="{lexeme}",
        lexTarget="word",
        level=0, flow="col", wrap=False, strectch=False,
    ),
    word=dict(
        template=True,
        features="gap",
        base=True,
        level=0, flow="col", wrap=False, strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
