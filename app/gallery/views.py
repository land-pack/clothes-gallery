import os
from flask import render_template, redirect, request, flash, current_app, url_for, abort, send_from_directory
from werkzeug import secure_filename
from . import gallery
from .forms import ImageForm, CategoryForm
from ..models import Image, Category
from app import db


@gallery.route('/')
def index():
    return render_template('gallery/index.html')


@gallery.route('/add-category', methods=['GET', 'POST'])
def add_category():
    form = CategoryForm()
    if request.method == 'POST':
        if form.name.data:
            category_name = form.name.data
            category = Category(name=category_name)
            db.session.add(category)
            db.session.commit()
            return redirect(url_for('gallery.upload'))
        else:
            return redirect(url_for('.add_category'))
    return render_template('gallery/add-category.html', form=form)


@gallery.route('/album/')
def album():
    albums = Category.query.all()  # Get a list of the Category
    if albums is None:
        abort(404)

    # image = albums[0].images.order_by(Image.timestamp.desc()).first()
    images = []
    for album in albums:
        Image.query.filter_by(category_id=album.id).first()

    size_album = len(albums)
    return render_template('gallery/album.html', size_album=size_album, albums=albums, image=images)


@gallery.route('/contact')
def contact():
    return render_template('gallery/contact.html')


@gallery.route('/upload', methods=['GET', 'POST'])
def upload():
    form = ImageForm()
    if request.method == 'POST':
        if form.image.data.filename and form.category.data:
            filename = secure_filename(form.image.data.filename)
            personal_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], str(form.category.data.id))
            if not os.path.exists(personal_dir):
                os.mkdir(personal_dir)

            image_url = os.path.join(personal_dir, filename)
            form.image.data.save(image_url)
            image = Image(name=form.name.data, category=str(form.category.data), url=image_url, filename=filename,
                          category_id=form.category.data.id)

            cat = Category.query.filter_by(id=form.category.data.id).first()
            cat.add_one(filename)  # Update the album counter by call instance method!
            db.session.add(cat)
            db.session.add(image)
            db.session.commit()
            return redirect(url_for('gallery.album'))
        else:
            return redirect(url_for('.upload'))

    return render_template('gallery/upload.html', form=form)


@gallery.route('/lists/<category_id>')
def lists(category_id):
    album = Category.query.filter_by(id=category_id).first()
    images = album.images.order_by(Image.timestamp.desc())
    return render_template('gallery/lists.html', images=images)


@gallery.route('/heads/<category>/<filename>')
def send_image(category, filename):
    # personal_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], category)
    personal_dir = current_app.config['UPLOAD_FOLDER'] + '/' + category + '/'
    return send_from_directory(personal_dir, filename)
