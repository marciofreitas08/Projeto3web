from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    municipio_escolhido = request.args.get("municipio")
    if (municipio_escolhido == None):
        imposto = [f"https://impostometro.com.br/widget/contador/es"]
    else:
        imposto = [f"https://impostometro.com.br/widget/contador/es?municipio={municipio_escolhido}"]
    return render_template("index.html", impostos=imposto)

@app.route('/mapa')
def info():

    return render_template("mapa.html")

if __name__ == '__main__':
    app.run(debug=True)
