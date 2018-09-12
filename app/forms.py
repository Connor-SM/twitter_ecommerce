from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SubmitField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class PostForm(FlaskForm):
    post = StringField('Tweet...', validators=[DataRequired()])
    submit = SubmitField('Post')
