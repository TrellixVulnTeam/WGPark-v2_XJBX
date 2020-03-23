from flask_restful import Resource, reqparse
from model.valor import ValorModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('descricao', type=str, required=True, help="Campo 'descricao' não pode ser nulo.")
argumentos.add_argument('valor', type=str, required=True, help="Campo 'valor' não pode ser nulo.")

class ValorController(Resource):

    def get(self, pkcodvalor):

        valor = ValorModel.read_valor(pkcodvalor)

        if valor:
            return {'message': valor.json()}
            
        return {'message': 'Valor não encontrado!'}, 404

    def post(self, pkcodvalor):

        dados = argumentos.parse_args()
        valor = ValorModel(**dados)
        
        try:

            valor.create_valor()
            return{'message': 'Valor cadastrado com sucesso!',
                    'info': valor.json()}

        except Exception as erro:
            return {'message': str(erro)}, 400

    def put(self, pkcodvalor):

        dados = argumentos.parse_args()
        valor = ValorModel.read_valor(pkcodvalor)

        if valor:

            valor.update_valor(**dados)
            valor.create_valor()

            return {'message': 'Valor editado com sucesso!'}

        return {'message': 'Valor não encontrado!'}, 404

    def delete(self, pkcodvalor):

        valor = ValorModel.read_valor(pkcodvalor)

        if valor:
            
            valor.delete_valor()
            return {'message': 'Valor deletado com sucesso!'}

        return {'message': 'Valor não encontrado!'}, 404
