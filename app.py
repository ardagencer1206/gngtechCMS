import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, HeroContent, Patent, JobPosting
from forms import HeroContentForm, PatentForm, JobPostingForm

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

# Veritabanı objesini uygulamaya bağlıyoruz
db.init_app(app)

# Uygulama başlarken tabloları ve varsayılan veriyi oluştur
with app.app_context():
    db.create_all()
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

# --- ROTASLAR (ROUTES) ---

@app.route('/')
def index():
    hero = HeroContent.query.first()
    patents = Patent.query.all()
    return render_template('index.html', hero=hero, patents=patents)

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
        
    patents = Patent.query.all()
    jobs = JobPosting.query.all()
    return render_template('admin.html', form=form, patents=patents, jobs=jobs)

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

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
