from flask import Flask
app = Flask(__name__)

from rakurakudinokun import get_ovo

@app.route("/")
def hello():
    ovo = get_ovo()
    ovo.rachar()
    return '<html><h1>%s</h1></html>' % unicode(ovo)

if __name__ == '__main__':
    print 'Iniciando'
    app.run(debug=True)
    print 'Terminado'
