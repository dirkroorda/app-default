from os.path import dirname, abspath

API_VERSION = 1
# To let Text-Fabric check whether its version matches the version of the TF-app

# PROVENANCE_SPEC = dict()
#
# Here follow the provenance parameters,
# which are used to fetch data and to report provenance in data exports.
# Do not specify values if the defaults work for you.
# The values set here are also the defaults.
#
# NB: zero configuration might already work for your corpus!
#
PROVENANCE_SPEC = dict(
    org="annotation",
    # The GitHub organisation name under which your TF data resides
    #
    repo="default",
    # The GitHub repo name under which your TF data resides
    # N.B. org/repo = annotation/default acts as placeholder for app-less datasets
    #
    relative="tf",
    # The path inside the repo to the directory
    # that holds the version directories of the tf data.
    #
    graphics=None,
    # If not None, it is the path inside the repo to the directory
    # that holds the graphics files
    #
    version="0.1",
    # The version directory with the actual `tf` files that will be used.
    #
    moduleSpecs=None,
    # You can specify modules that should always be loaded with the core data,
    # as many as you want:
    #
    # moduleSpecs = (
    #     dict(
    #         org="researcher1",
    #         repo="work1",
    #         relative="tf",
    #         corpus="speicalism1",
    #         docUrl=(
    #             "{nbUrl}/researcher1/work1/blob/master/programs/specialism1.ipynb"
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
    #             "{nbUrl}/researcher2/work2/blob/master/programs/specialism2.ipynb"
    #         ),
    #         doiText="uu.vvvv/archive.wwwwwww",
    #         doiUrl="https://doi.org/uu.vvvv/archive.wwwwwww",
    #     ),
    # )
    #
    # If modules have the same org or repo as the main data, these do not have to
    # be specified.
    #
    zip=None,
    # only used by `text-fabric-zip` when collecting data into zip files
    # as attachments to a GitHub release.
    # If left to `None`, will be configured to use the main repo and the modules.
    # It will then also fetch the graphics.
    #
    # You can specify the main repo, modules, and related data:
    #
    # zip=["repo"]
    # Only the main module.
    #
    # zip=["repo", "mod1", "mod2"]
    # if org and relative for the modules are the same as for are the main repo)
    #
    # in general it should be:
    #
    # zip=["repo"] + [("org1", "mod1", "relative1"), ("org2", "mod2", "relative2")]
    #
    # When the value is `None`, this value is used
    # where all modules mentioned in the moduleSpecs will be filled in.
    #
    # You can also use this scheme to include other data from the repository.
    # Note that graphics data will be packaged automatically.
    #
    #
    corpus="TF dataset (unspecified)",
    # A user-friendly name for your corpus
    #
    doi=None,
    # If your data is archived: the doi of the archived version, like
    # "xx.yyyy/archive.zzzzzzz"
    # without the https://doi.org/ in front.
    #
    webBase=None,
    # If present, the base url for an online instantiation of the corpus
    #
    webLang=None,
    # If passed, the language in which section headings must be generated in web links
    #
    webUrl=None,
    # If present, webLink(node) will use this as a template to generate a url
    # to an online instantation of the node.
    #
    # The following place holders will be honoured:
    # {base}: the webBase above
    # <1> : value for section heading 1
    # <2> : value for section heading 2
    # <3> : value for section heading 3
    # {version}: version of the TF resource
    #
    webUrlLex=None,
    # If passed, webLink(node) will use this as a template to generate a url
    # to an online instantation of the lexeme node.
    #
    # The following place holders will be honoured:
    # {base}: the webBase above
    # {lid} : value for the id of the lexeme
    # {version} version of the TF resource
    #
    webLexId=None,
    # If present, it is either:
    # the name of a feature that contains the lexeme id for lexeme nodes.
    #
    # or True and then the app should implement app.getLexId(n) that computes lexeme ids
    # for lexeme nodes.
    #
    # The lexeme id is the one used in the online instantiation of the corpus
    # to point to lexemes.
    #
    # If the value
    #
    webHint=None
    # If passed, will be used as hint text when the user hovers over a web link
)

# DOCS = dict()
#
# Here follow the parameters for documentation.
# Do not specify values if the defaults work for you.
# The values set here are also the defaults.
#
# NB: zero configuration might already work for your corpus!
#
# in the settings below you may refer to provenance settings, like {org} and {repo}
# You may refer to nbviewer with {urlNb}
#
DOCS = dict(
    docRoot="{urlGh}",
    # Where the docs are: on Github (default), or on nbviewer ("{urlNb}") or somewhere else.
    #
    docExt=".md",
    # The extension of documentation pages
    #
    docBase="{docRoot}/{org}/{repo}/blob/master/docs",
    # Base url page for the corpus documentation
    #
    docPage="home",
    # Landing page for the corpus documentation
    #
    featureBase=None,
    # URL template for feature by feature documentation
    # `{tfDoc}` will be replaced by the root location of the documentation as set above.
    # The variable part `{feature}` will be replaced by the names of the features.
    #
    # The default is: "{docBase}/features/{feature}{docExt}"
    #
    featurePage="home",
    # Start page for feature documentation,
    # will be filled in into `FEATURE_URL` for the variable `{feature}`.
    #
    writing="",
    # code for triggering special fonts, e.g.
    # akk: akkadian
    # hbo: hebrew
    # syc: syriac
    # ara: arabic
    # grc: greek
    # cld: neo aramaic
    #
    charUrl="{tfDoc}/Writing/Transcription/",
    # Start page for character coding documentation.
    # TF supports several writing systems with character- and transcription tables.
    # Replace `Transcription` by the writing system relevant for your data.
    # `{tfDoc}` will be replaced by the root location of the online TF documentation.
    #
    # If it is left out, it will point to the transcription table in the TF docs
    # that corresponds with the writing setting.
    #
    charText="How TF features represent text",
    # Hint text when a user hovers over the `CHAR_URL` link
    #
)

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
    excludedFeatures=set(),
    # features that are present in the data source but will not be loaded for the TF browser
    #
    sectionSep1=" ",
    # separator between main and secondary sections in a passage reference;
    # e.g. the space in `Genesis 1:1`
    #
    sectionSep2=":",
    # separator between secondary and tertiary sections in a passage reference;
    # e.g. the `:` in `Genesis 1:1`
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
    exampleSectionHtml="<code>piece 1</code>",
    # Formatted placeholder text for passage entry fields in the TF browser.
    #
    exampleSection="piece 1",
    # Placeholder text for passage entry fields in the TF browser.
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
        lexOcc="slot",
        # If present, indicates that this is a lexeme type,
        # and it points to the type of things that are occurrences of lexemes.
        # Lexemes are displayed with an indication of their first and last occurrence.
        #
        # There is no default.
        #
        lineNumber=None,
        # If present, it should be the name of a feature that holds source line numbers.
        #
        graphics=None,
        # If present and True, then there is additional graphics available for nodes of this
        # type.
        # The app needs to define a function
        #
        # getGraphics(nodee, nodeType, isOuter) => HTML code for sourcing the graphics
        #
        # See uruk.
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
    sign=dict(featuresBare="feat1", features="feat3"),
)

# INTERFACE_DEFAULTS = dict()
#
# The following options can be passed to plain and pretty
# They can also be set in the Text-Fabric Browser.
# The values set here are also the defaults.
# Do not specify values if the defaults work for you.
# NB: zero configuration might already work for your corpus!
# Here their app-dependent defaults can be specified.
# Not all options work for all corpora.
#
INTERFACE_DEFAULTS = dict(
    # first the options that are available for all apps
    #
    withTypes=False,
    # whether to show the node type in plain and pretty displays
    #
    prettyTypes=True,
    # if withTypes is True, you can set prettyTypes=False to prevent
    # showing the types in pretty displays
    withNodes=False,
    # whether to show the node numbers in plain and pretty displays
    #
    showFeatures=True,
    # whether to show features and their values in pretty displays
    #
    # now the app dependent options
    #
    lineNumbers=None,
    # whether to show the line numbers in plain and pretty displays.
    # The line numbers come from the source files from which the TF dataset
    # has been generated.
    #
    # Those types for which lineNumber="feat" has been configured in TYPE_DISPLAY
    # will cause plain and pretty to display a source line number, which will
    # come from the feature feat.
    #
    showGraphics=None,
    # whether to show additional graphics in plain and pretty displays.
    # Only node types for which graphics=True has been configured in TYPE_DISPLAY
    # will cause plain and pretty to display those graphic elements.
)


def deliver():
    return (globals(), dirname(abspath(__file__)))
