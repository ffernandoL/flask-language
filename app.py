from flask import Flask, render_template, request, redirect
app = Flask(__name__)

languages = ['Python']

@app.route('/')
def index():
    return render_template('index.html', 
        languages=languages)

@app.route('/lang/<int:id>')
def languag(id):
    lang = languages[id]
    return render_template(
        'index.html',
        languag=lang,
        id=id
    )

@app.route('/add', methods=['POST'])
def add():
    language = request.form['language']
    languages.append(language)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    del languages[id]
    return redirect('/')

if __name__ == '__main__':
    app.run()