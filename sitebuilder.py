from collections import defaultdict
from datetime import datetime
import random
import sys
import os

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.update(
  FLATPAGES_ROOT='songs',
  FLATPAGES_EXTENSION = '.md'
)
songs = FlatPages(app)
freezer = Freezer(app)

song_colors = [
  '#FD7632',
  '#477C90',
  '#4B0082',
  '#CD4640',
  '#85D817',
  '#DDB8C7',
  '#2AC8C6',
]

def _annotate(song, i):
  if hasattr(song, 'slug'):
    return
  slug = os.path.basename(song.path)
  song.src = '/static/mp3/' + slug + '.mp3'
  song.slug = slug
  song.dt = datetime.strptime(song.meta['date'], '%Y/%m/%d')
  _add_color(song, i)

def _add_color(song, i):
  song.color = song_colors[i % len(song_colors)]

@app.route('/')
def index():
  for i, song in enumerate(songs):
    _annotate(song, i)

  sorted_songs = sorted(list(songs), key=lambda song: song.dt, reverse=True)

  # Re-add the colors once the songs are sorted.
  for i, song in enumerate(sorted_songs):
    _add_color(song, i)

  return render_template('index.html', songs=sorted_songs)

@app.route('/<path:path>/')
def song(path):
  related = defaultdict(list)

  song = songs.get_or_404(path)
  _annotate(song, random.randrange(0, len(song_colors)))

  for tag in song.meta['tags']:
    for i, s in enumerate(songs):
      if tag in s.meta['tags']:
        _annotate(s, i)
        if s.slug != song.slug:
          related[tag].append(s)
  song.related = related
  song.src = '/static/mp3/' + os.path.basename(path) + '.mp3'
  return render_template('song.html', song=song, title=song.meta['title'])

if __name__ == '__main__':
  if len(sys.argv) > 1 and sys.argv[1] == 'build':
    freezer.freeze()
  else:
    app.run()
