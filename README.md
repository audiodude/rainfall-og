# Rainfall
A pleasant way to self host mp3s as a static site.

This is the static site generator setup that powers [songs.travisbriggs.com](https://songs.travisbriggs.com).

It is written with lots of help from
[this fabulous article](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)

It uses Python, [Flask](http://flask.pocoo.org/), [Flask-FlatPages](https://pythonhosted.org/Flask-FlatPages/) and
[Frozen-Flask](https://pythonhosted.org/Frozen-Flask/).

**IMPORTANT NOTE: By default, this application is setup to store metadata about songs but not the songs themselves. Please back up your songs somewhere else**

## Getting Started
First, create a [virtualenv] to store the libraries needed by Rainfall. Next, install the requirements using pip:

`$ pip install -r requirements.txt`

To run the app and preview what your site looks like, use the `flask run` command. You will optionally want to set `FLASK_DEBUG` to 1 (true) if you plan on making changes to the templates or Python code:

`$ FLASK_DEBUG=1 FLASK_APP=sitebuilder.py flask run`

This command will print out a `http://localhost:5000` URL that you can use to preview your site.

## Adding songs

You will need a song, and something to say about the song.

Put the song in static/mp3/<slug>.mp3, where `<slug>` is the URL slug you want your song to show up at. For example:
  
`static/mp3/somewhere-over-the-rainbow.mp3`

Now create a [Markdown](https://en.wikipedia.org/wiki/Markdown) file (this is the same format that Reddit and Github use) in the `songs/` directory, with the same base filename as your song (slug) but with a .md extension. For example:

`songs/somewhere-over-the-rainbow.md`

### Contents of the markdown file

The markdown file contains what is called "front matter" at the top, which is just metadata about the song such as it's title. Underneath that is the description of the song, which can contain any markdown syntax or HTML.

[Here](https://raw.githubusercontent.com/audiodude/songs.travisbriggs.com/master/songs/bit-bop-three-1.md) is an example of a finished markdown file. You can use it as a template for your own songs. The duration is in milliseconds. The tags are used to show related songs on the song's listen page
