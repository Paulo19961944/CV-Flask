from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    data_nascimento = date(1996, 4, 24)  # Exemplo de data de nascimento
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return render_template('index.html', idade=idade)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
