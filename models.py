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

class Patent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patent_num = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    title_tr = db.Column(db.String(255), nullable=False)
    title_en = db.Column(db.String(255), nullable=False)
    desc_tr = db.Column(db.Text, nullable=False)
    desc_en = db.Column(db.Text, nullable=False)

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_tr = db.Column(db.String(255), nullable=False)
    title_en = db.Column(db.String(255), nullable=False)
    description_tr = db.Column(db.Text, nullable=False)
    description_en = db.Column(db.Text, nullable=False)
    requirements_tr = db.Column(db.Text, nullable=False)
    requirements_en = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

class LeadershipContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_a_tr = db.Column(db.String(100), nullable=False, default="Zihinler")
    title_a_en = db.Column(db.String(100), nullable=False, default="The minds")
    title_b_tr = db.Column(db.String(100), nullable=False, default="arkasındaki.")
    title_b_en = db.Column(db.String(100), nullable=False, default="behind it.")
    intro_tr = db.Column(db.Text, nullable=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.")
    intro_en = db.Column(db.Text, nullable=False, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.")

class LeadershipMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.String(10), nullable=False, default="001")
    initials = db.Column(db.String(10), nullable=False, default="LI")
    name = db.Column(db.String(100), nullable=False)
    role_tr = db.Column(db.String(100), nullable=False)
    role_en = db.Column(db.String(100), nullable=False)
    bio_tr = db.Column(db.Text, nullable=False)
    bio_en = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
