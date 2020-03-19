from flask_restful import Resource, reqparse
from model.carro import CarroModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('placa', type=str, required=True, help="Campo 'placa' não pode ser nulo.")
argumentos.add_argument('modelo', type=str, required=True, help="Campo 'modelo' não pode ser nulo.")

class CarroController(Resource):

    def get(self, placa):

        carro = CarroModel.read_carro(placa)

        if carro:
            return {'message': carro.json()}
            
        return {'message': 'Carro não encontrado!'}, 404

    def post(self, placa):

        dados = argumentos.parse_args()
        carro = CarroModel(**dados)
        
        try:

            carro.create_carro()
            return{'message': 'Carro cadastrado com sucesso!',
                    'info': carro.json()}

        except Exception as erro:
            return {'message': str(erro)}, 400

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
