from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from config_swagger import config_swagger
from controller.carro import Carros, Carro
from controller.valor import Valores, Valor
from controller.tipo_usuario import TipoUsuarios, TipoUsuario
from controller.status import StatusList, Status
from controller.usuario import Usuarios, Usuario
from controller.servico import Servicos, Servico
from model.carro import CarroModel
from model.valor import ValorModel
from model.tipo_usuario import TipoUsuarioModel
from model.status import StatusModel
from model.usuario import UsuarioModel
from model.servico import ServicoModel

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
    StatusModel.create_table()
    UsuarioModel.create_table()
    ServicoModel.create_table()
    lista_config = config_swagger()    
    app.register_blueprint(lista_config[0], url_prefix=lista_config[1])

#############################################################################################################
api.add_resource(Carros, '/carros')
api.add_resource(Carro, '/carro/<string:placa>')
api.add_resource(Valores, '/valores')
api.add_resource(Valor, '/valor/<int:pkcodvalor>')
api.add_resource(TipoUsuarios, '/tipousuarios')
api.add_resource(TipoUsuario, '/tipousuario/<int:pkcodtipo>')
api.add_resource(StatusList, '/statuslist')
api.add_resource(Status, '/status/<int:pkcodstatus>')
api.add_resource(Usuarios, '/usuarios')
api.add_resource(Usuario, '/usuario/<int:pkcodusuario>')
api.add_resource(Servicos, '/servicos')
api.add_resource(Servico, '/servico/<int:pkcodservico>')
#############################################################################################################
if __name__ == '__main__':
    
    app.run(debug=True)