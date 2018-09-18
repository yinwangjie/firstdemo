from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired,Length
from flask_wtf import Form

class CommentForm(Form):    #字段、检验器、表单组成flask_wtf
    name = StringField(
        'Name',
        validators=[DataRequired(),Length(max=255)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])