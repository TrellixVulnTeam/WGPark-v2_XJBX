from flask_restful import Resource, reqparse
from model.tipo_usuario import TipoUsuarioModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('descricao', type=str, required=True, help="Campo 'descricao' não pode ser nulo.")

class TipoUsuarioController(Resource):

    def get(self, descricao):

        tipo_usuario = TipoUsuarioModel.read_tipo(descricao)

        if tipo_usuario:
            return {'message': tipo_usuario.json()}
            
        return {'message': 'TipoUsuario não encontrado!'}, 404

    def post(self, descricao):

        dados = argumentos.parse_args()
        tipo_usuario = TipoUsuarioModel(**dados)
        
        try:

            tipo_usuario.create_tipo()
            return{'message': 'TipoUsuario cadastrado com sucesso!',
                    'info': tipo_usuario.json()}

        except Exception as erro:
            return {'message': str(erro)}, 400

    def put(self, descricao):

        dados = argumentos.parse_args()
        tipo_usuario = TipoUsuarioModel.read_tipo(descricao)

        if tipo_usuario:

            tipo_usuario.update_tipo(**dados)
            tipo_usuario.create_tipo()

            return {'message': 'TipoUsuario editado com sucesso!'}

        return {'message': 'TipoUsuario não encontrado!'}, 404

    def delete(self, descricao):

        tipo_usuario = TipoUsuarioModel.read_tipo(descricao)

        if tipo_usuario:
            
            tipo_usuario.delete_tipo()
            return {'message': 'TipoUsuario deletado com sucesso!'}

        return {'message': 'TipoUsuario não encontrado!'}, 404
