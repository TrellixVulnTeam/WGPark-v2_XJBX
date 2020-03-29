from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from config_swagger import config_swagger
from controller.carro import Carros, Carro
from controller.valor import ValorController
from controller.tipo_usuario import TipoUsuarioController
from model.carro import CarroModel
from model.valor import ValorModel
from model.tipo_usuario import TipoUsuarioModel

#############################################################################################################
app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
CORS(app)
api = Api(app)

#############################################################################################################
@app.before_first_request
def cria_banco():

    CarroModel.create_table()
    ValorModel.create_table()
    TipoUsuarioModel.create_table()
    lista_config = config_swagger()    
    app.register_blueprint(lista_config[0], url_prefix=lista_config[1])

#############################################################################################################
api.add_resource(Carros, '/carros')
api.add_resource(Carro, '/carro/<string:placa>')
api.add_resource(ValorController, '/valor/<int:pkcodvalor>')
api.add_resource(TipoUsuarioController, '/tipousuario/<string:descricao>')

#############################################################################################################
if __name__ == '__main__':
    
    app.run(debug=True)