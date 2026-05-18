from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
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

class LeadershipContentForm(FlaskForm):
    title_a_tr = StringField('Başlık Kısım 1 (TR)', validators=[DataRequired()])
    title_a_en = StringField('Başlık Kısım 1 (EN)', validators=[DataRequired()])
    title_b_tr = StringField('Başlık Kısım 2 (TR)', validators=[DataRequired()])
    title_b_en = StringField('Başlık Kısım 2 (EN)', validators=[DataRequired()])
    intro_tr = TextAreaField('Açıklama (TR)', validators=[DataRequired()])
    intro_en = TextAreaField('Açıklama (EN)', validators=[DataRequired()])
    submit = SubmitField('Güncelle')

class LeadershipMemberForm(FlaskForm):
    order_num = StringField('Sıra No (örn: 001)', validators=[DataRequired()])
    initials = StringField('İnisiyaller (örn: LI)', validators=[DataRequired()])
    name = StringField('İsim ve Unvan', validators=[DataRequired()])
    role_tr = StringField('Rol (TR)', validators=[DataRequired()])
    role_en = StringField('Rol (EN)', validators=[DataRequired()])
    bio_tr = TextAreaField('Biyografi (TR)', validators=[DataRequired()])
    bio_en = TextAreaField('Biyografi (EN)', validators=[DataRequired()])
    is_active = BooleanField('Aktif', default=True)
    submit = SubmitField('Kaydet')

class InsightContentForm(FlaskForm):
    title_a_tr = StringField('Başlık İlk Kısım (TR)', validators=[DataRequired()])
    title_a_en = StringField('Başlık İlk Kısım (EN)', validators=[DataRequired()])
    title_b_tr = StringField('Başlık İkinci Kısım (TR)', validators=[DataRequired()])
    title_b_en = StringField('Başlık İkinci Kısım (EN)', validators=[DataRequired()])
    intro_tr = TextAreaField('Giriş Metni (TR)', validators=[DataRequired()])
    intro_en = TextAreaField('Giriş Metni (EN)', validators=[DataRequired()])
    submit = SubmitField('Kaydet')

class InsightArticleForm(FlaskForm):
    order_num = StringField('Sıra No', validators=[DataRequired()])
    image_file = FileField('Makale Görseli', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Sadece görseller (JPG, PNG) yüklenebilir.')])
    category_tr = StringField('Kategori (TR)', validators=[DataRequired()])
    category_en = StringField('Kategori (EN)', validators=[DataRequired()])
    date_tr = StringField('Tarih (TR)', validators=[DataRequired()])
    date_en = StringField('Tarih (EN)', validators=[DataRequired()])
    read_time_tr = StringField('Okuma Süresi (TR) - İsteğe Bağlı')
    read_time_en = StringField('Okuma Süresi (EN) - İsteğe Bağlı')
    title_tr = StringField('Başlık (TR)', validators=[DataRequired()])
    title_en = StringField('Başlık (EN)', validators=[DataRequired()])
    excerpt_tr = TextAreaField('Kısa Açıklama (TR) - İsteğe Bağlı')
    excerpt_en = TextAreaField('Kısa Açıklama (EN) - İsteğe Bağlı')
    content_tr = TextAreaField('Makale İçeriği (TR)')
    content_en = TextAreaField('Makale İçeriği (EN)')
    link = StringField('Dış Link (İsteğe Bağlı)')
    is_active = BooleanField('Aktif', default=True)
    submit = SubmitField('Kaydet')

class GalleryContentForm(FlaskForm):
    title_a_tr = StringField('Başlık İlk Kısım (TR)', validators=[DataRequired()])
    title_a_en = StringField('Başlık İlk Kısım (EN)', validators=[DataRequired()])
    title_b_tr = StringField('Başlık İkinci Kısım (TR)', validators=[DataRequired()])
    title_b_en = StringField('Başlık İkinci Kısım (EN)', validators=[DataRequired()])
    intro_tr = TextAreaField('Giriş Metni (TR)', validators=[DataRequired()])
    intro_en = TextAreaField('Giriş Metni (EN)', validators=[DataRequired()])
    submit = SubmitField('Kaydet')

class GalleryItemForm(FlaskForm):
    order_num = StringField('Sıra No', validators=[DataRequired()])
    image_file = FileField('Görsel', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Sadece görseller (JPG, PNG) yüklenebilir.')])
    caption_tr = StringField('Açıklama (TR) - İsteğe Bağlı')
    caption_en = StringField('Açıklama (EN) - İsteğe Bağlı')
    is_active = BooleanField('Aktif', default=True)
    submit = SubmitField('Kaydet')
