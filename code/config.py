from os.path import dirname, abspath

API_VERSION = 1
# To let Text-Fabric check whether its version matches the version of the TF-app

PROTOCOL = "http://"
# protocol for the local TF browser
HOST = "localhost"
# host for the local TF browser
PORT = dict(kernel=19699, web=9699)
# port for the local TF browser
# In a real app, replace these ports by a value not taken by any other TF app

ORG = "annotation"
# The GitHub organisation name under which your TF data resides

REPO = "default"
# The GitHub repo name under which your TF data resides
# N.B. org/repo = annotation/default acts as placeholder for app-less datasets

CORPUS = "TF dataset (unspecified)"
# A user-friendly name for your corpus

RELATIVE = "tf"
# The path inside the repo to the directory that holds the version directories of the tf data.

VERSION = "0.1"
# The version directory with the actual `tf` files that will be used.

DOI_TEXT = "xx.yyyy/archive.zzzzzzz"
# If your data is archived: the doi of the archived version

DOI_URL = "https://doi.org/xx.yyyy/archive.zzzzzzz"
# If your data is archived: the doi of the archived version as complete url

DOC_URL = (
    f"https://nbviewer.jupyter.org/github/{ORG}/{REPO}" f"/blob/master/docs/home.md"
)
# Landing page for the corpus documentation

FEATURE_URL = f"{DOC_URL}/features/{{feature}}.md"
# URL template for feature by feature documentation
# The variable part `{{feature}}` will be replaced by the names of the features.

DOC_INTRO = "0_features.md"
# Start page for feature documentation, will be filled in into `FEATURE_URL` for the variable `{{feature}}`.

CHAR_URL = "{tfDoc}/Writing/Transcription/"
# Start page for character coding documentation.
# TF supports several writing systems with character- and transcription tables.
# Replace `Transcription` by the writing system relevant for your data.
# `{tfDc}` will be replaced by the root location oof the online TF documentation.

CHAR_TEXT = "How TF features represent text"
# Hint text when a user hovers over the `CHAR_URL` link

MODULE_SPECS = ()
# You can specify modules that should always be loaded with the core data,
# as many as you want:
#
# MODULE_SPECS = (
#     dict(
#         org="researcher1",
#         repo="work1",
#         relative="tf",
#         corpus="speicalism1",
#         docUrl=(
#             "https://nbviewer.jupyter.org/github/researcher1/work1"
#             "/blob/master/programs/specialism1.ipynb"
#         ),
#         doiText="xx.yyyy/archive.zzzzzzz",
#         doiUrl="https://doi.org/xx.yyyy/archive.zzzzzzz",
#     ),
#     dict(
#         org="researcher2",
#         repo="work2",
#         relative="tf",
#         corpus="speicalism2",
#         docUrl=(
#             "https://nbviewer.jupyter.org/github/researcher2/work2"
#             "/blob/master/programs/specialism2.ipynb"
#         ),
#         doiText="uu.vvvv/archive.wwwwwww",
#         doiUrl="https://doi.org/uu.vvvv/archive.wwwwwww",
#     ),
# )

ZIP = None
# only used by `text-fabric-zip` when collecting data into zip files
# as attachments to a GitHub release.
# If left to `None`, will be configured to use the main repo and the modules.

# You can specify the main repo, modules, and related data:
#
# ZIP = [REPO]
# Only the main module.

# ZIP = [REPO] + [m["repo"] for m in MODULE_SPECS]
# if org and relative for the modules are the same as for are the main repo)
#
# in general it should be:
# ZIP = [REPO] + [(m["org"], m["repo"], m["relative"]) for m in MODULE_SPECS]
# This is equivalent to leaving the value to `None`.
#
# And if there is other data, e.g. image data in the main repo:
# ZIP = [REPO, (ORG, REPO, 'sources/cdli/images')]

EXAMPLE_SECTION = "<code>piece 1</code>"
# Formatted placeholder text for passage entry fields in the TF browser.

EXAMPLE_SECTION_TEXT = "piece 1"
# Placeholder text for passage entry fields in the TF browser.

# DATA_DISPLAY = dict()
#
# Here follow generic display parameters, none of which have to be filled in.
# Do not specify values if the defaults work for you.
# The values set here are also the defaults.
#
# NB: zero configuration might already work for your corpus!
#
DATA_DISPLAY = dict(
    noneValues={None},
    #
    # feature values that are deemed uninformative, e.g. `None`, `'NA'`
    #
    sectionSep1=" ",
    # separator between main and secondary sections in a passage reference;
    # e.g. the space in `Genesis 1:1`
    #
    sectionSep2=":",
    # separator between secondary and tertiary sections in a passage reference;
    # e.g. the `:` in `Genesis 1:1`
    #
    writing="",
    # code for triggering special fonts, e.g.
    # cun: cuneiform
    # hbo: hebrew
    # syc: syriac
    # ara: arabic
    # grc: greek
    # cld: neo aramaic
    #
    textFormats={},
    # textFormats={"layout-orig-full": "layoutRich"},
    # additional text formats that can use HTML styling.
    # Keys: names of new text formats.
    # Values: name of a method that implements that format.
    # If the name is `xxx`,
    # then `app.py` should implement a method `fmt_xxx(node)`
    # to produce html for node `node`
    #
    browseNavLevel=2,
    # the section level up to which the browser shows a hierarchical tree.
    # Either 1 or 2
    #
    # The default is one less than the number of section types
    #
    browseContentPretty=False,
    # whether the content is shown as a list of subsectional items
    # contained in the selected item
    # or as a pretty display of the item itself
    #
)

# TYPE_DISPLAY = dict()
#
# Here follow display parameters per type
# If some types do not need configuration, you may leave them out.
# Do not specify values if the defaults work for you.
# NB: zero configuration might already work for your corpus!
#
TYPE_DISPLAY = dict(
    piece=dict(
        template="{title}",
        # node information for plain and pretty displays
        # You can have features filled in by mentioning them by name in the template, e.g.
        # `{name1} - {name2}`
        # You can also lookup feature values for upper nodes, e.g.
        # `{lex:gloss}`
        # which will look for a `lex` node above the current node
        # and retrieve its `gloss` value.
        # If you specify `True`, the node information will be the result of:
        # section and structure types nodes: a heading
        # other nodes: plain text of the node
        #
        # The default is:
        # True for the slot type and section and structure types
        # True for the section and structure types
        # "" for all other types
        #
        featuresBare="feat1 feat2",
        # pretty displays: which features to display by value only
        # (the feature name is not mentioned)
        #
        # The default = ""
        #
        features="feat3 feat4",
        # pretty displays: which features to display as name=value
        #
        # The default = ""
        #
        children="slot",
        # plain and pretty: which type of children to be included in the display.
        # The value should be a node type or a set of node types:
        # children={"piece", "slot"}.
        #
        # The default is:
        # for section and structure types: the type that comes immediately below it;
        # where the lowest section/structure type
        # have the biggest other type as child type or, if there is no such one:
        # the slotType.
        # The smallest other type has the slot type as child type.
        # Lexeme types do not have children.
        #
        verselike=False,
        # whether this type should be formatted as a verse
        #
        # The default is:
        # True for the lowest section type, if there are section types in otext.tf
        # But more types can be declared as verselike, e.g. `half_verse` in the bhsa
        #
        condense=True,
        # If present and true: this type is the default condense type.
        # pretty: when displaying tuples of nodes,
        # they will be chunked in displays of nodes of this type.
        #
        # The default is:
        # True for the lowest section type, if there are section types in otext.tf
        # If there is no such section, we pick a medium-sized type.
        # If there are no such types, we pick the slot type, but this is pathological.
        #
        base=False,
        # If present and True: this type acts as the base type:
        # plain: if the node needs to be highlighted, it gets a coloured background.
        # plain: Nodes of other types receive their highlights
        # as coloured borders around their boxes.
        # pretty: Children of these nodes are not expanded further,
        # but displayed in plain mode (with highlighting)
        #
        # The default is:
        # True for the slot type.
        #
        lexTarget="slot",
        # If present, indicates that this is a lexeme type,
        # and it points to the type of things that have lexemes.
        # Lexemes are displayed with an indication of their first and last occurrence.
        #
        # There is no default.
        #
        level=1,
        # pretty: the visual style of the container box of this node, values 0, 1, 2, 3.
        # The bigger the number, the heavier the borders of the boxes.
        # The default is:
        # 3 for types known as section or structure types, including the verselike types
        # 0 for the slot type and types known as lexeme types
        # 1 or 2 for the remaining types:
        # the bigger types are 2
        # the smaller types are 1
        #
        flow="row",
        # pretty: whether the container should arrange its subdisplays
        # as a column or as a row.
        # Values: row, col
        # The default is:
        # col if level is 3 (typically section types), except for the verselike types
        # col if level is 0 (typically slot types and lexeme types)
        # row if level is 1 or 2 (typically linguistic types at sentence level) and
        # for the verselike types
        #
        wrap=True,
        # pretty: whether the children may be wrapped.
        # The default is:
        # True if the children form a row, such rows may be wrapped
        # False if the children form a column,
        # such columns may not be wrapped (into several columns)
        # For some types in uruk it is needed to deviate from the default.
        #
        stretch=True,
        # pretty: whether the children should be stretched
        # in the direction perpendicular to their stacking.
        # The default is:
        # True if the children form a row (then each child is stretched vertically)
        # False if the children form a column
        # (then each child is NOT stretched horizontally)
        # For some types in uruk it is needed to deviate from the default.
        #
    ),
    sign=dict(
        featuresBare="feat1",
        features="feat3",
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
