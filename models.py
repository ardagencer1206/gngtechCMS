from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HeroContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_line1_tr = db.Column(db.String(100), nullable=False, default="Görünmeyeni")
    title_line1_en = db.Column(db.String(100), nullable=False, default="Imaging the")
    title_line2_tr = db.Column(db.String(100), nullable=False, default="görüntülemek.")
    title_line2_en = db.Column(db.String(100), nullable=False, default="invisible.")
    location_tr = db.Column(db.String(100), nullable=False, default="ODTÜ Teknokent · Ankara")
    location_en = db.Column(db.String(100), nullable=False, default="METU Technopark · Ankara")
    caption_tr = db.Column(db.Text, nullable=False, default="Lorem ipsum dolor sit amet...")
    caption_en = db.Column(db.Text, nullable=False, default="Lorem ipsum dolor sit amet...")
