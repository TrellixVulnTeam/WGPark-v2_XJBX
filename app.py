from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from config_swagger import config_swagger
from controller.carro import CarroController
from model.carro import CarroModel

#############################################################################################################
app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
CORS(app)
api = Api(app)

#############################################################################################################
@app.before_first_request
def cria_banco():
    CarroModel.create_table()
    lista_config = config_swagger()    
    app.register_blueprint(lista_config[0], url_prefix=lista_config[1])

#############################################################################################################
api.add_resource(CarroController, '/carro')

#############################################################################################################
if __name__ == '__main__':
    app.run(debug=True)