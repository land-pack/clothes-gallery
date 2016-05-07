from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo, Optional, DataRequired
from wtforms import ValidationError
from flask_wtf.file import FileField


class ImageForm(Form):
    name = StringField('Name', validators=[Length(1, 64)])
    category = SelectField('Category',
                           choices=[('Fashion', 'Fashion'), ('Headshots', 'Headshots'), ('T-shift', 'T-shift')],
                           validators=[DataRequired()]
                           )
    image = FileField('Your photo')
    submit = SubmitField('Upload')

