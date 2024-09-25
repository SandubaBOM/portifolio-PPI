from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Rota principal que redireciona para a página inicial '/home'
@app.route('/')
def index():
    return redirect(url_for('home'))

# Rota para a página inicial
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/experiencias')
def pagina_experiencias():
    return render_template('experiencias.html')

if __name__ == '__main__':
    # Executa o aplicativo Flask com o modo de depuração ativado
    app.run(debug=True)
