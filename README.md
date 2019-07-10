<div>
<img src="images/logo.png" align="right" width="200"/>
<img src="images/tf.png" align="right" width="200"/>
<img src="images/dans.png" align="right" width="100"/>
</div>

# Default TF app

This is the
[Text-Fabric](https://githubv.com/annotation/text-fabric)
default app for working with a TF corpus.

If you write a TF app, copy this whole repo to a new repo `app-xxx`,
where `xxx` is your name for the corpus.

Then:

*   adjust the logo in `code/static`;
*   adjust the stuff in `code/config.py`:
    *   the ORG and REPO informationA;
    *   the ports (make them different from all other TF-apps);
*   (optionally): adjust the code for the functions in `code/app.py` if you want special behaviour for your corpus;
*   (optionally): adjust the css code `code/static/display.css` if you want special behaviour for your corpus;
*   (optionally): write a tutorial: `start.ipynb`, meant for `annotation/tutorials/{CORPUS}`;
*   adapt this Readme file:
    *   leave out these instructions
    *   replace {CORPUS} (corpus name) and {ORG} and {REPO} etc. with the appropriate values;
    *   place a link to the provenance description of your corpus (probably `docs/About.md` in your corpus repo);
    *   place a link to the feature documentation of your corpus (probably `docs/transcription.md` in your corpus repo);
    *   (optionally): get a Zenodo badge and fill in the url in the Zenodo link below;
    *   (optionally): let the Software Heritage Archive harvest your app and adjust the link in the SHA badge below.
    *   (optionally): make a screenshot and put it in `images/shot.png` in this repo

It offers this [API](https://annotation.github.io/text-fabric/Api/App/).

# Readme template

[![sha](sha.png) Software Heritage Archive](https://archive.softwareheritage.org/browse/origin/https://github.com/annotation/app-default/)

[![DOI](https://zenodo.org/badge/nnn.svg)](https://zenodo.org/badge/latestdoi/nnn)

## Name of the corpus

This is a
[Text-Fabric](https://githubv.com/annotation/text-fabric) app
for working with the
[{CORPUS}](https://github.com/{ORG}/{REPO}) corpus: {SHORT DESC}

Get started with the
[tutorial](https://nbviewer.jupyter.org/github/annotation/tutorials/blob/master/{CORPUS}/start.ipynb).

It offers this [API](https://annotation.github.io/text-fabric/Api/App/).

![shot](images/shot.png)

