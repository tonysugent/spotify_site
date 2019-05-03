from flask import Flask
from flask.ext.via import Via

app = Flask(__name__)
app.config['VIA_ROUTES_MODULE'] = 'routes'

via = Via()

via.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)