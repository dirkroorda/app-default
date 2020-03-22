from tf.core.helpers import mdhtmlEsc, htmlEsc
from tf.applib.helpers import dh
from tf.applib.display import prettyPre, getFeatures
from tf.applib.highlight import hlText, hlRep
from tf.applib.api import setupApi
from tf.applib.links import outLink

SECTION = {"document", "section", "paragraph"}  # should be the three section levels
SLOT = "word"


class TfApp(object):
    def __init__(*args, **kwargs):
        setupApi(*args, **kwargs)

    def webLink(app, n, text=None, className=None, _asString=False, _noUrl=False):
        api = app.api
        T = api.T

        (document, section, paragraph) = T.sectionFromNode(n, fillup=True)
        passageText = app.sectionStrFromNode(n)
        href = "#" if _noUrl else app.docUrl
        if text is None:
            text = passageText
            title = f"show this passage online"
        else:
            title = passageText
        if _noUrl:
            title = None
        target = "" if _noUrl else None

        result = outLink(
            text,
            href,
            title=title,
            className=className,
            target=target,
            passage=passageText,
        )
        if _asString:
            return result
        dh(result)

    def fmt_layoutRich(app, n):
        api = app.api
        F = api.F
        after = f'{F.punc.v(n) or ""} '
        isGap = F.gap.v(n)
        material = F.letters.v(n) or ""
        layout = f'<span class="gap">{material}</span>' if isGap else material
        return f"{layout}{after}"

    def _plain(
        app, n, passage, isLinked, _asString, secLabel, **options,
    ):
        display = app.display
        d = display.get(options)

        _asApp = app._asApp
        api = app.api
        F = api.F
        L = api.L
        T = api.T

        nType = F.otype.v(n)
        result = passage
        if _asApp:
            nodeRep = f' <a href="#" class="nd">{n}</a> ' if d.withNodes else ""
        else:
            nodeRep = f" <i>{n}</i> " if d.withNodes else ""

        rep = ""
        text = ""
        if nType == SLOT:
            text = hlText(app, [n], d.highlights, fmt=d.fmt)
        elif nType in {"paragraph"}:
            text = hlText(app, L.d(n, otype=SLOT), d.highlights, fmt=d.fmt)
        elif nType in SECTION:
            if secLabel and d.withPassage:
                sep1 = app.sectionSep1
                sep2 = app.sectionSep2
                label = (
                    "{}"
                    if nType == "document"
                    else f"{{}}{sep1}{{}}"
                    if nType == "section"
                    else f"{{}}{sep1}{{}}{sep2}{{}}"
                )
                rep = label.format(*T.sectionFromNode(n))
                rep = mdhtmlEsc(rep)
                rep = hlRep(app, rep, n, d.highlights)
                if isLinked:
                    rep = app.webLink(n, text=f"{rep}&nbsp;", _asString=True)
            else:
                rep = ""
            if nType == "paragraph":
                rep += mdhtmlEsc(f"{nType} {F.number.v(n)}") if secLabel else ""
            elif nType == "section":
                rep += mdhtmlEsc(f"{nType} {F.number.v(n)}") if secLabel else ""
            elif nType == "document":
                rep += mdhtmlEsc(f"{nType} {F.title.v(n)}") if secLabel else ""
            rep = hlRep(app, rep, n, d.highlights)
            if text:
                text = hlRep(app, text, n, d.highlights)
        else:
            rep = hlText(app, L.d(n, otype=SLOT), d.highlights, fmt=d.fmt)
        if text:
            tClass = display.formatClass[d.fmt].lower()
            text = f'<span class="{tClass}">{text}</span>'
            rep += text
        rep = app._addLink(
            n, rep, nodeRep, isLinked=isLinked and not passage and nType not in SECTION,
        )
        result += rep

        if _asString or _asApp:
            return result
        dh(result)

    def _addLink(app, n, rep, nodeRep, isLinked=None):
        if isLinked:
            rep = app.webLink(n, text=rep, _asString=True)
        theLine = ""
        return f"{rep}{nodeRep}{theLine}"

    def _pretty(
        app, n, outer, html, firstSlot, lastSlot, **options,
    ):
        display = app.display
        d = display.get(options)

        goOn = prettyPre(app, n, firstSlot, lastSlot, d)
        if not goOn:
            return
        (
            slotType,
            nType,
            isBigType,
            className,
            boundaryClass,
            hlAtt,
            nodePart,
            myStart,
            myEnd,
        ) = goOn

        api = app.api
        F = api.F
        L = api.L
        T = api.T
        isHtml = options.get("fmt", None) in app.textFormats

        (hlClass, hlStyle) = hlAtt

        heading = ""
        featurePart = ""
        children = ()

        if isBigType:
            children = ()
        elif nType == "document":
            children = L.d(n, otype="section")
        elif nType == "section":
            children = L.d(n, otype="paragraph")
        elif nType == "paragraph":
            children = L.d(n, otype=SLOT)
        else:
            children = L.d(n, otype=SLOT)

        isText = False

        if nType == "document":
            heading = htmlEsc(F.title.v(n))
            heading += " "
            heading += getFeatures(app, n, ("author",), plain=True, **options,)
        elif nType == "section":
            heading = htmlEsc(F.number.v(n))
            featurePart = getFeatures(app, n, (), **options,)
        elif nType == "paragraph":
            heading = htmlEsc(F.number.v(n))
            featurePart = getFeatures(app, n, (), **options,)
        elif nType == slotType:
            isText = True
            text = T.text(n, fmt=d.fmt)
            heading = text if isHtml else htmlEsc(text)
            featurePart = getFeatures(app, n, (), withName=True, **options,)

        tClass = display.formatClass[d.fmt].lower() if isText else app.defaultCls
        heading = f'<span class="{tClass}">{heading}</span>'

        if outer:
            typePart = app.webLink(n, text=f"{nType} {heading}", _asString=True)
        else:
            typePart = heading

        label = (
            f"""
    <div class="lbl {className}">
        {typePart}
        {nodePart}
    </div>
"""
            if typePart or nodePart
            else ""
        )

        html.append(
            f"""
<div class="contnr {className} {hlClass}" {hlStyle}>
    {label}
    <div class="meta">
        {featurePart}
    </div>
"""
        )
        if children:
            html.append(
                f"""
    <div class="children {className}">
"""
            )

        for ch in children:
            app._pretty(
                ch, False, html, firstSlot, lastSlot, **options,
            )
        if children:
            html.append(
                """
    </div>
"""
            )
        html.append(
            """
</div>
"""
        )
