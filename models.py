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

class InsightContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_a_tr = db.Column(db.String(100), nullable=False, default="Yayımlanmış")
    title_a_en = db.Column(db.String(100), nullable=False, default="Research,")
    title_b_tr = db.Column(db.String(100), nullable=False, default="araştırmalar.")
    title_b_en = db.Column(db.String(100), nullable=False, default="published.")
    intro_tr = db.Column(db.Text, nullable=False, default="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore.")
    intro_en = db.Column(db.Text, nullable=False, default="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore.")

class InsightArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.String(10), nullable=False, default="001")
    image_file = db.Column(db.String(255), nullable=True) # Optional for now, fallback to default if None
    category_tr = db.Column(db.String(50), nullable=False)
    category_en = db.Column(db.String(50), nullable=False)
    date_tr = db.Column(db.String(50), nullable=False)
    date_en = db.Column(db.String(50), nullable=False)
    read_time_tr = db.Column(db.String(50), nullable=True) # Optional
    read_time_en = db.Column(db.String(50), nullable=True) # Optional
    title_tr = db.Column(db.String(200), nullable=False)
    title_en = db.Column(db.String(200), nullable=False)
    excerpt_tr = db.Column(db.Text, nullable=True)
    excerpt_en = db.Column(db.Text, nullable=True)
    content_tr = db.Column(db.Text, nullable=True)
    content_en = db.Column(db.Text, nullable=True)
    link = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True)

class GalleryContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_a_tr = db.Column(db.String(100), nullable=False, default="Tarayıcıdan")
    title_a_en = db.Column(db.String(100), nullable=False, default="From the")
    title_b_tr = db.Column(db.String(100), nullable=False, default="kareler.")
    title_b_en = db.Column(db.String(100), nullable=False, default="scanner.")
    intro_tr = db.Column(db.Text, nullable=False, default="At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos.")
    intro_en = db.Column(db.Text, nullable=False, default="At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos.")

class GalleryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_num = db.Column(db.String(10), nullable=False, default="001")
    image_file = db.Column(db.String(255), nullable=False)
    caption_tr = db.Column(db.String(255), nullable=True)
    caption_en = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True)

class ContactContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_a_tr = db.Column(db.String(100), default="Let's")
    title_a_en = db.Column(db.String(100), default="Let's")
    title_b_tr = db.Column(db.String(100), default="konuşalım.")
    title_b_en = db.Column(db.String(100), default="talk.")
    intro_tr = db.Column(db.Text, default="Lorem ipsum dolor sit amet...")
    intro_en = db.Column(db.Text, default="Lorem ipsum dolor sit amet...")
    headline_a_tr = db.Column(db.String(100), default="ODTÜ Teknokent,")
    headline_a_en = db.Column(db.String(100), default="METU Technopark,")
    headline_b_tr = db.Column(db.String(100), default="Ankara.")
    headline_b_en = db.Column(db.String(100), default="Ankara.")
    address_label_tr = db.Column(db.String(100), default="Adres")
    address_label_en = db.Column(db.String(100), default="Address")
    address_value_tr = db.Column(db.Text, default="ODTÜ Teknokent, A Blok")
    address_value_en = db.Column(db.Text, default="METU Technopark, Block A")
    general_label_tr = db.Column(db.String(100), default="Genel Sorular")
    general_label_en = db.Column(db.String(100), default="General Inquiries")
    general_email = db.Column(db.String(100), default="hello@gngtechnology.com")
    press_label_tr = db.Column(db.String(100), default="Basın & Partnerlik")
    press_label_en = db.Column(db.String(100), default="Press & Partnerships")
    press_email = db.Column(db.String(100), default="partners@gngtechnology.com")
    phone_label_tr = db.Column(db.String(100), default="Telefon")
    phone_label_en = db.Column(db.String(100), default="Phone")
    phone_number = db.Column(db.String(50), default="+90 312 123 45 67")
    coords_label_tr = db.Column(db.String(100), default="Koordinatlar")
    coords_label_en = db.Column(db.String(100), default="Coordinates")
    coords_value_tr = db.Column(db.String(100), default="39.8917° K · 32.7833° D")
    coords_value_en = db.Column(db.String(100), default="39.8917° N · 32.7833° E")
    map_pin_title_tr = db.Column(db.String(100), default="● GNG · ODTÜ Teknokent")
    map_pin_title_en = db.Column(db.String(100), default="● GNG · METU Technopark")
    map_pin_sub_tr = db.Column(db.String(100), default="A Blok · 39.8917° K · 32.7833° D")
    map_pin_sub_en = db.Column(db.String(100), default="Block A · 39.8917° N · 32.7833° E")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False, default='todo') # todo, in_progress, review, done
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    progress = db.Column(db.Integer, default=0) # 0 to 100
    assignee = db.Column(db.String(100), nullable=True)
    order = db.Column(db.Integer, default=0)
