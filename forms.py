from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class HeroContentForm(FlaskForm):
    title_line1_tr = StringField('Başlık Satır 1 (TR)', validators=[DataRequired()])
    title_line1_en = StringField('Başlık Satır 1 (EN)', validators=[DataRequired()])
    title_line2_tr = StringField('Başlık Satır 2 (TR)', validators=[DataRequired()])
    title_line2_en = StringField('Başlık Satır 2 (EN)', validators=[DataRequired()])
    location_tr = StringField('Konum (TR)', validators=[DataRequired()])
    location_en = StringField('Konum (EN)', validators=[DataRequired()])
    caption_tr = TextAreaField('Açıklama (TR)', validators=[DataRequired()])
    caption_en = TextAreaField('Açıklama (EN)', validators=[DataRequired()])
    submit = SubmitField('Güncelle')
