from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
url = 'http://0.0.0.0:3000/transacciones'
@app.route('/templates')
def template():
    return render_template('template.html')

@app.route('/', methods=['POST', 'GET'])
def generarMovimiento():
    if request.method == 'POST':
        umaiz = int(request.form['maiz'])
        ucocoa = int(request.form['cocoa'])
        uarroz = int(request.form['arroz'])
        tipo = request.form['tipoMovimiento']
        valor = umaiz*5000 + ucocoa*8000 + uarroz*4000
        detalles = "Unidades de maiz a 5000: "+str(umaiz)+" \nUnidades de cocoa a 8000: "+str(ucocoa)+" \n Unidades de arroz a 4000: "+str(uarroz)
        cliente = request.form['cliente']
        
        payload = {'type': tipo, 'value': valor, 'detalles': detalles, 'cliente': cliente}
        print(payload)
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            return "Transacción realizada exitosamente"
        else: 
            return "Error: " + str(response.status_code)
    else:
        return render_template('crearTransaccion.html')
    
app.run(host='0.0.0.0',port=8000)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
