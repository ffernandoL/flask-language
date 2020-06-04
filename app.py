from flask import Flask, render_template, request, redirect
app = Flask(__name__)

languages = ['Python']

@app.route('/')
def index():
    return render_template('index.html', languages=languages)

@app.route('/add', methods=['POST'])
def add():
    language = request.form['language']
    languages.append(language)
    return redirect('/')

if __name__ == '__main__':
    app.run()