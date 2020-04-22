from flask_restful import Resource, reqparse, ResponseBase
from model.carro import CarroModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('placa', type=str, required=True, help="Campo 'placa' não pode ser nulo.")
argumentos.add_argument('modelo', type=str, required=True, help="Campo 'modelo' não pode ser nulo.")

class Carros(Resource):

    def get(self):

        lista_carros = []
        carros = CarroModel.read_carros()
        
        if carros:

            for carro in carros:
    
                lista_carros.append(carro.json())

            return {'message': lista_carros}, 200
            
        return {'message': 'Carros não encontrados!'}, 404

    def post(self):

        dados = argumentos.parse_args()
        carro = CarroModel(**dados)

        if carro.read_carro(carro.placa):

            response = ResponseBase(response={'Carro já existe na base de dados!'}, 
                                    status=200, 
                                    headers={'location': '/carro/'+carro.placa})
            return response
        
        if carro.create_carro():
            response = ResponseBase(response={'Carro criado com sucesso!'}, 
                                    status=201, 
                                    headers={'location': '/carro/'+carro.placa})
            return response

        else:
            response = ResponseBase(response={'Erro ao salvar Carro!'}, 
                                    status=500)
            return response

class Carro(Resource):

    def get(self, placa):
        
        carro = CarroModel.read_carro(placa)

        if carro:
            return {'message': carro.json()}
            
        return {'message': 'Carro não encontrado!'}, 404

    def put(self, placa):

        dados = argumentos.parse_args()
        carro = CarroModel.read_carro(placa)

        if carro:

            carro.update_carro(**dados)
            carro.create_carro()

            return {'message': 'Carro editado com sucesso!'}

        return {'message': 'Carro não encontrado!'}, 404

    def delete(self, placa):

        carro = CarroModel.read_carro(placa)

        if carro:
            
            carro.delete_carro()
            return {'message': 'Carro deletado com sucesso!'}

        return {'message': 'Carro não encontrado!'}, 404