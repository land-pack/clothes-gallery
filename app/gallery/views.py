from flask import render_template
from . import gallery


@gallery.route('/')
def index():
    return render_template('gallery/index.html')


@gallery.route('/album')
def album():
    return render_template('gallery/album.html')


@gallery.route('/contact')
def contact():
    return render_template('gallery/contact.html')


@gallery.route('/upoad')
def upload():
    return render_template('gallery/upload.html')
