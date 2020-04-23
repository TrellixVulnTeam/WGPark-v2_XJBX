from flask_restful import Resource, reqparse, ResponseBase
from model.usuario import UsuarioModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome', type=str, required=True, help="Campo 'nome' não pode ser nulo.")
argumentos.add_argument('cpf', type=str, required=True, help="Campo 'cpf' não pode ser nulo.")
argumentos.add_argument('fkcodtipousuario', type=int, required=True, help="Campo 'fkcodtipousuario' não pode ser nulo.")


class Usuarios(Resource):

    def get(self):

        lista_usuarios = []
        usuarios = UsuarioModel.read_usuarios()
        
        if usuarios:

            for usuario in usuarios:
    
                lista_usuarios.append(usuario.json())

            return {'message': lista_usuarios}, 200
            
        return {'message': 'Usuarios não encontrados!'}, 404

    def post(self):

        dados = argumentos.parse_args()
        usuario = UsuarioModel(**dados)

        if usuario.read_usuario(usuario.cpf):

            response = ResponseBase(response={'Usuario já existe na base de dados!'}, 
                                    status=200, 
                                    headers={'location': '/usuario/'+usuario.cpf})
            return response
        
        if usuario.create_usuario():
            response = ResponseBase(response={'Usuario criado com sucesso!'}, 
                                    status=201, 
                                    headers={'location': '/usuario/'+usuario.cpf})
            return response

        else:
            response = ResponseBase(response={'Erro ao salvar Usuario!'}, 
                                    status=500)
            return response

class Usuario(Resource):

    def get(self, cpf):
        
        usuario = UsuarioModel.read_usuario(cpf)

        if usuario:
            return {'message': usuario.json()}
            
        return {'message': 'Usuario não encontrado!'}, 404

    def put(self, cpf):

        dados = argumentos.parse_args()
        usuario = UsuarioModel.read_usuario(cpf)

        if usuario:

            usuario.update_usuario(**dados)
            return {'message': 'Usuario editado com sucesso!'}

        return {'message': 'Usuario não encontrado!'}, 404

    def delete(self, cpf):

        usuario = UsuarioModel.read_usuario(cpf)

        if usuario:
            
            usuario.delete_usuario()
            return {'message': 'Usuario deletado com sucesso!'}

        return {'message': 'Usuario não encontrado!'}, 404