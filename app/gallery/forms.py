from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo, Optional, DataRequired
from wtforms import ValidationError
from flask_wtf.file import FileField
from ..models import Category


def enabled_categories():
    return Category.query.all()


class ImageForm(Form):
    name = StringField('Name', validators=[Length(1, 64)])
    category = QuerySelectField(query_factory=enabled_categories, get_label='name', allow_blank=True,
                                validators=[DataRequired()])

    @classmethod
    def category_choice(cls):
        choices = [(x.id, str(x.name)) for x in Category.query.all()]
        cls.lazy_value = choices

    image = FileField('Your photo', validators=[Required(), DataRequired()])
    submit = SubmitField('Upload')


class CategoryForm(Form):
    name = StringField('New Category Name', validators=[Length(1, 64)])
    submit = SubmitField('Add Category')
