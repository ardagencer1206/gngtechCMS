from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField
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

class PatentForm(FlaskForm):
    patent_num = StringField('Patent No (örn: PATENT · TR-2024/0001)', validators=[DataRequired()])
    status = SelectField('Durum', choices=[('granted', 'Tescilli'), ('pending', 'Beklemede'), ('filed', 'Başvuru')], validators=[DataRequired()])
    title_tr = StringField('Başlık (TR)', validators=[DataRequired()])
    title_en = StringField('Başlık (EN)', validators=[DataRequired()])
    desc_tr = TextAreaField('Açıklama (TR)', validators=[DataRequired()])
    desc_en = TextAreaField('Açıklama (EN)', validators=[DataRequired()])
    submit = SubmitField('Kaydet')

class JobPostingForm(FlaskForm):
    title_tr = StringField('İş Başlığı (TR)', validators=[DataRequired()])
    title_en = StringField('İş Başlığı (EN)', validators=[DataRequired()])
    description_tr = TextAreaField('Görev Tanımı (TR)', validators=[DataRequired()])
    description_en = TextAreaField('Görev Tanımı (EN)', validators=[DataRequired()])
    requirements_tr = TextAreaField('Yetkinlikler (TR)', validators=[DataRequired()])
    requirements_en = TextAreaField('Yetkinlikler (EN)', validators=[DataRequired()])
    is_active = BooleanField('Aktif İlan', default=True)
    submit = SubmitField('Kaydet')
