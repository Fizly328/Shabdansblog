from flask import Flask, render_template
import datetime

app = Flask(__name__)



@app.route('/')
@app.route('/index/')
def index():
    current_year = datetime.datetime.now().strftime("%Y")
    context = {
        'icon': "/static/img/main_icon.png",
        'name': 'Главная',
        'year': current_year,
        'age': int(current_year) - 2011
    }
    return render_template('index.html', **context)

@app.route('/contacts/')
def contacts():
    current_year = datetime.datetime.now().strftime("%Y")
    context = {
        'icon': "/static/img/call.png",
        'name': 'Контакты',
        'year': current_year
    }
    return render_template('contacts.html', **context)

@app.route('/blog/')
def blog():
    current_year = datetime.datetime.now().strftime("%Y")
    context = {
        'icon': "/static/img/blog.png",
        'name': 'Блог',
        'year': current_year
    }
    return render_template('blog.html', **context)
if __name__ == "__main__":
    app.run()
