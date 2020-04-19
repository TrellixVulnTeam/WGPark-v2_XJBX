from flask_restful import Resource, reqparse, ResponseBase
from model.valor import ValorModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('descricao', type=str, required=True, help="Campo 'descricao' não pode ser nulo.")
argumentos.add_argument('valor', type=str, required=True, help="Campo 'valor' não pode ser nulo.")

class Valores(Resource):

    def get(self):

        lista_valores = []
        valores = ValorModel.read_valores()

        if valores:

            for valor in valores:

                lista_valores.append(valor.json())

            return {'message': lista_valores}, 200
            
        return {'message': 'Valores não encontrados!'}, 404

    def post(self):

        dados = argumentos.parse_args()
        valor = ValorModel(**dados)
        
        if valor.read_valor(valor.descricao):

            response = ResponseBase(response={'Valor já existe na base de dados!'}, 
                                    status=200, 
                                    headers={'location': '/valor/'+ valor.descricao})
            return response
        
        try:

            valor.create_valor()
            response = ResponseBase(response={'Carro criado com sucesso!'}, 
                                    status=201, 
                                    headers={'location': '/valor/'+ valor.descricao})
            return response

        except Exception as erro:
            response = ResponseBase(response={erro}, 
                                    status=500)
            return response

class Valor(Resource):

    def get(self, descricao):

        valor = ValorModel.read_valor(descricao)

        if valor:
            return {'message': valor.json()}
        
        return {'message': 'Valor não encontrado!'}, 404

    def put(self, descricao):

        dados = argumentos.parse_args()
        valor = ValorModel.read_valor(descricao)

        if valor:

            valor.update_valor(**dados)
            valor.create_valor()

            return {'message': 'Valor editado com sucesso!'}

        return {'message': 'Valor não encontrado!'}, 404

    def delete(self, descricao):

        valor = ValorModel.read_valor(descricao)

        if valor:
            
            valor.delete_valor()
            return {'message': 'Valor deletado com sucesso!'}

        return {'message': 'Valor não encontrado!'}, 404
