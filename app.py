from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = '$#FhEdge123'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/barangmasuk')
def barangmasuk():
    return render_template('barangmasuk.html')

@app.route('/barangkeluar')
def barangkeluar():
    return render_template('barangkeluar.html')

@app.route('/laporanmasuk')
def laporanmasuk():
    return render_template('laporanmasuk.html')

@app.route('/laporankeluar')
def laporankeluar():
    return render_template('laporankeluar.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__  == '__main__':
    app.run(debug=True)
