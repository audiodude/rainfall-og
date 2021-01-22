# Rainfall

A pleasant way to self host mp3s as a static site.

This is the static site generator setup that powers [songs.travisbriggs.com](https://songs.travisbriggs.com).

It is written with lots of help from
[this fabulous article](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/)

It uses Python, [Flask](http://flask.pocoo.org/), [Flask-FlatPages](https://pythonhosted.org/Flask-FlatPages/) and
[Frozen-Flask](https://pythonhosted.org/Frozen-Flask/).

**IMPORTANT NOTE: By default, this application is setup to store metadata about songs but not the songs themselves. Please back up your songs somewhere else**

## Getting Started

First, install Python 3 and create a [virtualenv](https://virtualenv.pypa.io/en/latest/) to store the libraries needed by Rainfall. Next, install the requirements using pip:

`$ pip install -r requirements.txt`

To run the app and preview what your site looks like, use the `flask run` command. You will optionally want to set `FLASK_DEBUG` to 1 (true) if you plan on making changes to the templates or Python code:

`$ FLASK_DEBUG=1 FLASK_APP=sitebuilder.py flask run`

This command will print out a `http://localhost:5000` URL that you can use to preview your site. By default your site will look a bit strange, it will be empty and have no songs in it. You can edit `templates/index.html` to change the header text and link (or anything else about the template; this is _your_ site).

## Adding songs

You will need a song, with a title, and something to say about the song.

Put the song in `static/mp3/<slug>.mp3`, where `<slug>` is the URL slug you want your song to show up at. For example:

`static/mp3/somewhere-over-the-rainbow.mp3`

Now create a [Markdown](https://en.wikipedia.org/wiki/Markdown) file (this is the same format that Reddit and Github use) in the `songs/` directory, with the same base filename as your song (slug) but with a .md extension. For example:

`songs/somewhere-over-the-rainbow.md`

If you reload your localhost:5000 page, you should see your song and be able to play it. When you click the song, you will be taken to `http://localhost:5000/somewhere-over-the-rainbow` where you will see your song's detailed listen page with its description.

### Contents of the markdown file

The markdown file contains what is called "front matter" at the top, which is just metadata about the song such as it's title. In fact, the only required front matter field is "title: [your title here]". Underneath that is the description of the song, which can contain any markdown syntax or HTML.

[Here](https://raw.githubusercontent.com/audiodude/songs.travisbriggs.com/master/songs/bit-bop-three-1.md) is an example of a finished markdown file. You can use it as a template for your own songs. The duration is in milliseconds. The tags are used to show related songs on the song's listen page

## Building your site

So far, we've been previewing our site locally using `flask run`. This works well for viewing our changes, or if we happen to have a Python server lying around, but to be honest, we probably won't be updating this site more than once a day at absolute maximum. Let's unleash the real power of Rainfall and generate a _static site_.

A static site means that the mp3s, all the HTML pages, and the Javascript and CSS have all been _pre-rendered_ and exist as static files. The main advantage of this is that we can then host the files extremely cheaply, and they will show up extremely fast (no Python server slowing things down).

To build the site, simply run:

`$ python sitebuilder.py build`

This will create a `build` subdirectory that contains the final rendered website. Whenever you make changes to the site generator (the files that you checked out from git), run that command again to render a new version of your site.

### Uploading the site to Netlify

[Netlify](https://www.netlify.com/) is a service that hosts static content, behind a CDN, with a custom domain name and LetsEncrypt SSL certificate, for free.

You can install [Netlify's CLI](https://www.netlify.com/docs/cli/) and then deploy your site using:

`$ netlify deploy`

The command line tool will walk you through the steps to authenticate your account and finish the deploy. From there, you can use the Netlify webapp to rename your site, attach a custom domain, and provision an HTTPS certificate.

## Questions?

If you have any questions, you can contact the author of this repository, Travis Briggs, at audiodude@gmail.com
