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

        if valor.read_valor_before_post(valor.descricao):
           
            response = ResponseBase(response={'Valor já existe na base de dados!'}, 
                                    status=200, 
                                    headers={'location': '/valor/' + str(valor.read_valor_before_post(valor.descricao))})
            return response
        
        if valor.create_valor():
            response = ResponseBase(response={'Valor criado com sucesso!'}, 
                                    status=201, 
                                    headers={'location': '/valor/' + str(valor.pkcodvalor)})
            return response

        else:
            response = ResponseBase(response={'Erro ao salvar Valor!'}, 
                                    status=500)
            return response

class Valor(Resource):

    def get(self, pkcodvalor):

        valor = ValorModel.read_valor(pkcodvalor)

        if valor:
            return {'message': valor.json()}
        
        return {'message': 'Valor não encontrado!'}, 404

    def put(self, pkcodvalor):

        dados = argumentos.parse_args()
        valor = ValorModel.read_valor(pkcodvalor)

        if valor:

            valor.update_valor(**dados)

            return {'message': 'Valor editado com sucesso!'}

        return {'message': 'Valor não encontrado!'}, 404

    def delete(self, pkcodvalor):

        valor = ValorModel.read_valor(pkcodvalor)

        if valor:
            
            valor.delete_valor()
            return {'message': 'Valor deletado com sucesso!'}

        return {'message': 'Valor não encontrado!'}, 404
