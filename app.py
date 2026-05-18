import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from models import db, HeroContent, Patent, JobPosting, LeadershipContent, LeadershipMember, InsightContent, InsightArticle, GalleryContent, GalleryItem, ContactContent
from forms import HeroContentForm, PatentForm, JobPostingForm, LeadershipContentForm, LeadershipMemberForm, InsightContentForm, InsightArticleForm, GalleryContentForm, GalleryItemForm, ContactContentForm

app = Flask(__name__)

# Railway ortamında oluşturulan SECRET_KEY değişkenini çekiyoruz
app.secret_key = os.environ.get('SECRET_KEY', 'default-dev-secret-key')

# MySQL bağlantı bilgilerini Railway Variable'larından (ortam değişkenlerinden) alıyoruz
db_user = os.environ.get('MYSQLUSER', 'root')
db_password = os.environ.get('MYSQLPASSWORD', '')
db_host = os.environ.get('MYSQLHOST', 'localhost')
db_port = os.environ.get('MYSQLPORT', '3306')
db_name = os.environ.get('MYSQLDATABASE', 'railway')

# Veritabanı URL'sini oluşturuyoruz
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads', 'insights')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['GALLERY_UPLOAD_FOLDER'] = os.path.join('static', 'uploads', 'gallery')
os.makedirs(app.config['GALLERY_UPLOAD_FOLDER'], exist_ok=True)

# Veritabanı objesini uygulamaya bağlıyoruz
db.init_app(app)

from sqlalchemy import text

# Uygulama başlarken tabloları ve varsayılan veriyi oluştur
with app.app_context():
    db.create_all()
    
    # Otomatik sütun ekleme (Migration yerine basit çözüm)
    try:
        db.session.execute(text('ALTER TABLE insight_article ADD COLUMN content_tr TEXT'))
        db.session.commit()
    except Exception:
        db.session.rollback()
        
    try:
        db.session.execute(text('ALTER TABLE insight_article ADD COLUMN content_en TEXT'))
        db.session.commit()
    except Exception:
        db.session.rollback()
        
    new_contact_columns = [
        "phone_label_tr VARCHAR(100)",
        "phone_label_en VARCHAR(100)",
        "phone_number VARCHAR(50)",
        "coords_label_tr VARCHAR(100)",
        "coords_label_en VARCHAR(100)",
        "coords_value_tr VARCHAR(100)",
        "coords_value_en VARCHAR(100)",
        "map_pin_title_tr VARCHAR(100)",
        "map_pin_title_en VARCHAR(100)",
        "map_pin_sub_tr VARCHAR(100)",
        "map_pin_sub_en VARCHAR(100)"
    ]
    for col in new_contact_columns:
        try:
            db.session.execute(text(f'ALTER TABLE contact_content ADD COLUMN {col}'))
            db.session.commit()
        except Exception:
            db.session.rollback()

    if not HeroContent.query.first():
        default_hero = HeroContent()
        db.session.add(default_hero)
        db.session.commit()
        
    if not Patent.query.first():
        default_patents = [
            Patent(patent_num='PATENT · TR-2024/0001', status='granted', title_tr='Lorem ipsum dolor sit amet adipiscing.', title_en='Lorem ipsum dolor sit amet adipiscing.', desc_tr='Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', desc_en='Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
            Patent(patent_num='PATENT · WO-2024/0042', status='pending', title_tr='Ut enim ad minim veniam quis nostrud.', title_en='Ut enim ad minim veniam quis nostrud.', desc_tr='Exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure.', desc_en='Exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure.'),
            Patent(patent_num='PATENT · EP-2024/0078', status='granted', title_tr='Duis aute irure dolor in reprehenderit.', title_en='Duis aute irure dolor in reprehenderit.', desc_tr='In voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat.', desc_en='In voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat.'),
            Patent(patent_num='PATENT · US-2024/0119', status='pending', title_tr='Cupidatat non proident sunt in culpa.', title_en='Cupidatat non proident sunt in culpa.', desc_tr='Qui officia deserunt mollit anim id est laborum sed ut perspiciatis unde omnis iste natus.', desc_en='Qui officia deserunt mollit anim id est laborum sed ut perspiciatis unde omnis iste natus.'),
            Patent(patent_num='PATENT · TR-2025/0203', status='filed', title_tr='Error sit voluptatem accusantium doloremque.', title_en='Error sit voluptatem accusantium doloremque.', desc_tr='Laudantium totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi.', desc_en='Laudantium totam rem aperiam eaque ipsa quae ab illo inventore veritatis et quasi.'),
            Patent(patent_num='PATENT · WO-2025/0314', status='pending', title_tr='Architecto beatae vitae dicta sunt explicabo.', title_en='Architecto beatae vitae dicta sunt explicabo.', desc_tr='Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit consequuntur.', desc_en='Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit consequuntur.')
        ]
        db.session.bulk_save_objects(default_patents)
        db.session.commit()

    if not LeadershipContent.query.first():
        default_leadership = LeadershipContent()
        db.session.add(default_leadership)
        db.session.commit()

    if not LeadershipMember.query.first():
        default_member = LeadershipMember(
            order_num="001",
            initials="LI",
            name="Lorem Ipsum, PhD",
            role_tr="CEO · Kurucu Ortak",
            role_en="CEO · Co-founder",
            bio_tr="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium.",
            bio_en="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium."
        )
        db.session.add(default_member)
        db.session.commit()

    if not InsightContent.query.first():
        default_insight_content = InsightContent()
        db.session.add(default_insight_content)
        db.session.commit()

    if not InsightArticle.query.first():
        default_article = InsightArticle(
            order_num="001",
            category_tr="Vaka Çalışması",
            category_en="Case Study",
            date_tr="21 Şub 2026",
            date_en="21 Feb 2026",
            read_time_tr="14 dk okuma",
            read_time_en="14 min read",
            title_tr="Örnek Makale Başlığı (Öne Çıkan)",
            title_en="Sample Article Title (Featured)",
            excerpt_tr="Bu örnek bir makale kısa açıklamasıdır.",
            excerpt_en="This is a sample article excerpt.",
            content_tr="Bu örnek bir makale tam içeriğidir. Admin panelinden düzenleyebilirsiniz.",
            content_en="This is a sample article full content. You can edit it from the admin panel.",
            link="#"
        )
        db.session.add(default_article)
        db.session.commit()

    if not GalleryContent.query.first():
        default_gallery_content = GalleryContent()
        db.session.add(default_gallery_content)
        db.session.commit()

    if not GalleryItem.query.first():
        default_gallery_item = GalleryItem(
            order_num="001",
            image_file="default_gallery.jpg",
            caption_tr="Örnek Görsel",
            caption_en="Sample Image"
        )
        db.session.add(default_gallery_item)
        db.session.commit()

    if not ContactContent.query.first():
        default_contact_content = ContactContent()
        db.session.add(default_contact_content)
        db.session.commit()

# --- ROTASLAR (ROUTES) ---

@app.route('/')
def index():
    hero = HeroContent.query.first()
    patents = Patent.query.all()
    leadership_content = LeadershipContent.query.first()
    leadership_members = LeadershipMember.query.filter_by(is_active=True).order_by(LeadershipMember.order_num).all()
    insight_content = InsightContent.query.first()
    insight_articles = InsightArticle.query.filter_by(is_active=True).order_by(InsightArticle.order_num).all()
    gallery_content = GalleryContent.query.first()
    gallery_items = GalleryItem.query.filter_by(is_active=True).order_by(GalleryItem.order_num).all()
    contact_content = ContactContent.query.first()
    return render_template('index.html', hero=hero, patents=patents, leadership_content=leadership_content, leadership_members=leadership_members, insight_content=insight_content, insight_articles=insight_articles, gallery_content=gallery_content, gallery_items=gallery_items, contact_content=contact_content)

@app.route('/insight/<int:id>')
def insight_detail(id):
    article = InsightArticle.query.get_or_404(id)
    if not article.is_active:
        return redirect(url_for('index'))
    return render_template('article.html', article=article)

@app.route('/career')
def career():
    hero = HeroContent.query.first()
    jobs = JobPosting.query.filter_by(is_active=True).all()
    return render_template('career.html', hero=hero, jobs=jobs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('admin'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'neuromag2':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Hatalı kullanıcı adı veya şifre!')
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    hero = HeroContent.query.first()
    form = HeroContentForm(obj=hero)
    
    if form.validate_on_submit():
        form.populate_obj(hero)
        db.session.commit()
        flash('Hero içeriği başarıyla güncellendi!')
        return redirect(url_for('admin'))
        
    leadership_content = LeadershipContent.query.first()
    leadership_form = LeadershipContentForm(obj=leadership_content)
    
    patents = Patent.query.all()
    jobs = JobPosting.query.all()
    leadership_members = LeadershipMember.query.all()
    
    insight_content = InsightContent.query.first()
    insight_form = InsightContentForm(obj=insight_content)
    insight_articles = InsightArticle.query.all()
    
    gallery_content = GalleryContent.query.first()
    gallery_form = GalleryContentForm(obj=gallery_content)
    gallery_items = GalleryItem.query.all()
    
    contact_content = ContactContent.query.first()
    contact_form = ContactContentForm(obj=contact_content)
    
    return render_template('admin.html', form=form, patents=patents, jobs=jobs, leadership_form=leadership_form, leadership_members=leadership_members, insight_form=insight_form, insight_articles=insight_articles, gallery_form=gallery_form, gallery_items=gallery_items, contact_form=contact_form)

@app.route('/admin/patent/add', methods=['GET', 'POST'])
def admin_patent_add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    form = PatentForm()
    if form.validate_on_submit():
        patent = Patent()
        form.populate_obj(patent)
        db.session.add(patent)
        db.session.commit()
        flash('Yeni patent başarıyla eklendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_patent.html', form=form, action="Ekle")

@app.route('/admin/patent/edit/<int:id>', methods=['GET', 'POST'])
def admin_patent_edit(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    patent = Patent.query.get_or_404(id)
    form = PatentForm(obj=patent)
    
    if form.validate_on_submit():
        form.populate_obj(patent)
        db.session.commit()
        flash('Patent başarıyla güncellendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_patent.html', form=form, action="Düzenle", patent=patent)

@app.route('/admin/patent/delete/<int:id>', methods=['POST'])
def admin_patent_delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    patent = Patent.query.get_or_404(id)
    db.session.delete(patent)
    db.session.commit()
    flash('Patent başarıyla silindi!')
    return redirect(url_for('admin'))

@app.route('/admin/career/add', methods=['GET', 'POST'])
def admin_career_add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    form = JobPostingForm()
    if form.validate_on_submit():
        job = JobPosting()
        form.populate_obj(job)
        db.session.add(job)
        db.session.commit()
        flash('Yeni iş ilanı başarıyla eklendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_career.html', form=form, action="Ekle")

@app.route('/admin/career/edit/<int:id>', methods=['GET', 'POST'])
def admin_career_edit(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    job = JobPosting.query.get_or_404(id)
    form = JobPostingForm(obj=job)
    
    if form.validate_on_submit():
        form.populate_obj(job)
        db.session.commit()
        flash('İş ilanı başarıyla güncellendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_career.html', form=form, action="Düzenle")

@app.route('/admin/career/delete/<int:id>', methods=['POST'])
def admin_career_delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    job = JobPosting.query.get_or_404(id)
    db.session.delete(job)
    db.session.commit()
    flash('İş ilanı başarıyla silindi!')
    return redirect(url_for('admin'))

@app.route('/admin/leadership_content/edit', methods=['POST'])
def admin_leadership_content_edit():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    leadership_content = LeadershipContent.query.first()
    form = LeadershipContentForm()
    
    if form.validate_on_submit():
        form.populate_obj(leadership_content)
        db.session.commit()
        flash('Liderlik giriş metni başarıyla güncellendi!')
        
    return redirect(url_for('admin'))

@app.route('/admin/leadership/add', methods=['GET', 'POST'])
def admin_leadership_add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    form = LeadershipMemberForm()
    if form.validate_on_submit():
        member = LeadershipMember()
        form.populate_obj(member)
        db.session.add(member)
        db.session.commit()
        flash('Yeni ekip üyesi başarıyla eklendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_leadership.html', form=form, action="Ekle")

@app.route('/admin/leadership/edit/<int:id>', methods=['GET', 'POST'])
def admin_leadership_edit(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    member = LeadershipMember.query.get_or_404(id)
    form = LeadershipMemberForm(obj=member)
    
    if form.validate_on_submit():
        form.populate_obj(member)
        db.session.commit()
        flash('Ekip üyesi başarıyla güncellendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_leadership.html', form=form, action="Düzenle")

@app.route('/admin/leadership/delete/<int:id>', methods=['POST'])
def admin_leadership_delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    member = LeadershipMember.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    flash('Ekip üyesi başarıyla silindi!')
    return redirect(url_for('admin'))


@app.route('/admin/insight_content/edit', methods=['POST'])
def admin_insight_content_edit():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    content = InsightContent.query.first()
    form = InsightContentForm()
    
    if form.validate_on_submit():
        form.populate_obj(content)
        db.session.commit()
        flash('Yayımlanmış Makaleler içeriği başarıyla güncellendi!')
        
    return redirect(url_for('admin'))

@app.route('/admin/insight/add', methods=['GET', 'POST'])
def admin_insight_add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    form = InsightArticleForm()
    if form.validate_on_submit():
        article = InsightArticle()
        form.populate_obj(article)
        
        if form.image_file.data:
            filename = secure_filename(form.image_file.data.filename)
            form.image_file.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            article.image_file = filename
            
        db.session.add(article)
        db.session.commit()
        flash('Yeni makale başarıyla eklendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_insight.html', form=form, action="Ekle")

@app.route('/admin/insight/edit/<int:id>', methods=['GET', 'POST'])
def admin_insight_edit(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    article = InsightArticle.query.get_or_404(id)
    form = InsightArticleForm(obj=article)
    
    if form.validate_on_submit():
        old_image = article.image_file
        form.populate_obj(article)
        
        if form.image_file.data:
            filename = secure_filename(form.image_file.data.filename)
            form.image_file.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            article.image_file = filename
        else:
            article.image_file = old_image
            
        db.session.commit()
        flash('Makale başarıyla güncellendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_insight.html', form=form, action="Düzenle", article=article)

@app.route('/admin/insight/delete/<int:id>', methods=['POST'])
def admin_insight_delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    article = InsightArticle.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Makale başarıyla silindi!')
    return redirect(url_for('admin'))

@app.route('/admin/gallery_content/edit', methods=['POST'])
def admin_gallery_content_edit():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    content = GalleryContent.query.first()
    form = GalleryContentForm()
    
    if form.validate_on_submit():
        form.populate_obj(content)
        db.session.commit()
        flash('Görsel Arşiv içeriği başarıyla güncellendi!')
        
    return redirect(url_for('admin'))

@app.route('/admin/gallery/add', methods=['GET', 'POST'])
def admin_gallery_add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    form = GalleryItemForm()
    if form.validate_on_submit():
        item = GalleryItem()
        form.populate_obj(item)
        
        if form.image_file.data:
            filename = secure_filename(form.image_file.data.filename)
            form.image_file.data.save(os.path.join(app.config['GALLERY_UPLOAD_FOLDER'], filename))
            item.image_file = filename
            
        db.session.add(item)
        db.session.commit()
        flash('Yeni görsel başarıyla eklendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_gallery.html', form=form, action="Ekle")

@app.route('/admin/gallery/edit/<int:id>', methods=['GET', 'POST'])
def admin_gallery_edit(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    item = GalleryItem.query.get_or_404(id)
    form = GalleryItemForm(obj=item)
    
    if form.validate_on_submit():
        old_image = item.image_file
        form.populate_obj(item)
        
        if form.image_file.data:
            filename = secure_filename(form.image_file.data.filename)
            form.image_file.data.save(os.path.join(app.config['GALLERY_UPLOAD_FOLDER'], filename))
            item.image_file = filename
        else:
            item.image_file = old_image
            
        db.session.commit()
        flash('Görsel başarıyla güncellendi!')
        return redirect(url_for('admin'))
        
    return render_template('admin_gallery.html', form=form, action="Düzenle", item=item)

@app.route('/admin/gallery/delete/<int:id>', methods=['POST'])
def admin_gallery_delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    item = GalleryItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Görsel başarıyla silindi!')
    return redirect(url_for('admin'))

@app.route('/admin/contact_content/edit', methods=['POST'])
def admin_contact_content_edit():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    content = ContactContent.query.first()
    form = ContactContentForm()
    
    if form.validate_on_submit():
        form.populate_obj(content)
        db.session.commit()
        flash('İletişim içeriği başarıyla güncellendi!')
        
    return redirect(url_for('admin'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
  
