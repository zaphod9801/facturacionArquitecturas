from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/templates')
def template():
    return render_template('template.html')

@app.route('/',methods=['GET'])
def listarTransacciones():
    transacciones_list = requests.get('http://0.0.0.0:3000/transacciones').json()
    saldo = 0
    for transaction in transacciones_list:
        if transaction['type'] == 'Entrada':
            saldo += transaction['value']
        else: 
            saldo -= transaction['value']
    return render_template('transacciones.html', transacciones=transacciones_list, saldo=saldo)
    
app.run(host='0.0.0.0',port=8000)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
