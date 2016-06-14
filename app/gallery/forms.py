# coding=utf-8
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
    name = StringField(u'衣服名称', validators=[Length(1, 64)])
    category = QuerySelectField(u'服装分类', query_factory=enabled_categories, get_label='name', allow_blank=True,
                                validators=[DataRequired()])

    @classmethod
    def category_choice(cls):
        choices = [(x.id, str(x.name)) for x in Category.query.all()]
        cls.lazy_value = choices

    image = FileField(u'衣服图像', validators=[Required(), DataRequired()])
    submit = SubmitField(u'添加一件')


class CategoryForm(Form):
    name = StringField(u'新的服饰分类', validators=[Length(1, 64)])
    sextype = SelectField(u'服饰选择', choices=[('boy', u'男装'), ('girl', u'女装'), ('part', u'配件')])
    submit = SubmitField(u'添加')
