from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo, Optional, DataRequired
from wtforms import ValidationError
from flask_wtf.file import FileField
from ..models import Category


def enabled_categories():
    # choices = [(x.id, str(x.name)) for x in Category.query.all()]
    # print choices
    # return choices
    return Category.query.all()


class ImageForm(Form):
    name = StringField('Name', validators=[Length(1, 64)])
    # category = SelectField('Category',
    #                        choices=[('Fashion', 'Fashion'), ('Headshots', 'Headshots'), ('T-shift', 'T-shift')],
    #                        validators=[DataRequired()]
    #                        )

    # category = QuerySelectField(queryset=Category.objects.all())
    category = QuerySelectField(query_factory=enabled_categories, get_label='name', allow_blank=True)

    # category = QuerySelectField(choices=enabled_categories, allow_blank=True)

    @classmethod
    def category_choice(cls):
        choices = [(x.id, str(x.name)) for x in Category.query.all()]
        cls.lazy_value = choices

    image = FileField('Your photo')
    submit = SubmitField('Upload')


class CategoryForm(Form):
    name = StringField('Name', validators=[Length(1, 64)])
    submit = SubmitField('Add Category')
