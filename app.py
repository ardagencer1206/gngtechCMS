import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Railway ortamında oluşturulan SECRET_KEY değişkenini çekiyoruz
app.secret_key = os.environ.get('SECRET_KEY', 'default-dev-secret-key')

# MySQL bağlantı bilgilerini Railway Variable'larından (ortam değişkenlerinden) alıyoruz
db_user = os.environ.get('MYSQLUSER', 'root')
db_password = os.environ.get('MYSQLPASSWORD', '')
db_host = os.environ.get('MYSQLHOST', 'localhost')
db_port = os.environ.get('MYSQLPORT', '3306')
db_name = os.environ.get('MYSQLDATABASE', 'railway')

# Veritabanı URL'sini oluşturuyoruz (PyMySQL sürücüsü ile)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Veritabanı objesini initialize ediyoruz (ileride tablo eklemek için hazır)
db = SQLAlchemy(app)

# --- ROTASLAR (ROUTES) ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Eğer zaten giriş yapılmışsa, direkt admin paneline yönlendir
    if session.get('logged_in'):
        return redirect(url_for('admin'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Kullanıcı adı ve şifre kontrolü (Şimdilik hardcode edilmiş durumda)
        if username == 'admin' and password == 'neuromag2':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Hatalı kullanıcı adı veya şifre!')
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/admin')
def admin():
    # Eğer kullanıcı giriş yapmamışsa, login sayfasına geri gönder
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('admin.html')

@app.route('/logout')
def logout():
    # Çıkış yap ve oturumu sonlandır
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Port numarası Railway'de dinamik olarak atanır.
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
