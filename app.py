from flask import Flask, render_template, request
import sqlite3
from datetime import date


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def conexao():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/espacos")
def espacos():

    busca = request.args.get('busca')
    tipo = request.args.get('tipo')
    conn = conexao()
    

    if busca and tipo:

        espacos = conn.execute('SELECT * FROM espaco WHERE nome LIKE ? AND tipo = ?', ('%' + busca + '%', tipo))

    elif busca:

        espacos = conn.execute('SELECT * FROM espaco WHERE nome LIKE ?', ('%' + busca + '%', ))

    elif tipo:

        espacos = conn.execute('SELECT * FROM espaco WHERE tipo = ?', (tipo,))

    else:

        espacos = conn.execute('SELECT * FROM espaco')

    return render_template("espacos.html", espacos = espacos)

@app.route("/disponibilidade")
def disponibilidade():
   
    tipo = request.args.get('tipo')
    data = request.args.get('data')
    conn = conexao()
    
    
    if not data:
        return render_template("disponibilidade.html", dados = [])
    
    if data and tipo:
        dados = conn.execute('''SELECT * from espaco LEFT JOIN reserva ON espaco.id = reserva.id_espaco 
                        AND reserva.data = ? WHERE espaco.nome = ? ''', (data, tipo))

    
    elif data:
        dados = conn.execute('''SELECT * from espaco LEFT JOIN reserva ON espaco.id = reserva.id_espaco 
            AND reserva.data = ?''', (data,))

    disponibilidade_horarios = []

    for dado in dados:
        linha = dict(dado)
        status_horarios = {
            'sala': linha['nome'], '7_830': 'livre', '830_10': 'livre', '10_1130': 'livre', '1130_13': 'livre',
            '13_1430': 'livre', '1430_16': 'livre', '16_1730': 'livre'
            
        }

        if linha['hora_inicio'] and linha['hora_fim']:

            if linha['hora_inicio'] >= '07:00' and linha['hora_fim'] <= '08:30':
                status_horarios['7_830'] = 'ocupado'


            elif linha['hora_inicio'] >= '08:30' and linha['hora_fim'] <= '10:00':
                status_horarios['830_10'] = 'ocupado'

            elif linha['hora_inicio'] >= '10:00' and linha['hora_fim'] <= '11:30':
                status_horarios['10_1130'] = 'ocupado'

            elif linha['hora_inicio'] >= '11:30' and linha['hora_fim'] <= '13:00':
                status_horarios['1130_13'] = 'ocupado'

            elif linha['hora_inicio'] >= '13:00' and linha['hora_fim'] <= '14:30':
                status_horarios['13_1430'] = 'ocupado'

            elif linha['hora_inicio'] >= '14:30' and linha['hora_fim'] <= '16:00':
                status_horarios['1430_16'] = 'ocupado'

            elif linha['hora_inicio'] >= '16:00' and linha['hora_fim'] <= '17:30':
                status_horarios['16_1730'] = 'ocupado'


        disponibilidade_horarios.append(status_horarios)

    print(disponibilidade_horarios)

    return render_template("disponibilidade.html", dados = disponibilidade_horarios)

@app.route("/fazer_reserva")
def fazerReserva():

    conn = conexao()
    
    

    return render_template("/fazer_reserva.html", teste = espacos)




















































app.run(debug=True, port=5000)