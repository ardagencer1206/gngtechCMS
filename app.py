import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db, HeroContent
from forms import HeroContentForm

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

# --- ROTASLAR (ROUTES) ---

@app.route('/')
def index():
    hero = HeroContent.query.first()
    return render_template('index.html', hero=hero)

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
        
    return render_template('admin.html', form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
