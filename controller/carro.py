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
            
        return {'message': 'Carro not found'}, 404

    def post(self, placa):

        dados = argumentos.parse_args()
        carro = CarroModel(**dados)
        
        try:

            carro.create_carro()
            return{'message': carro.json()}

        except Exception as erro:

            return {'message': str(erro)}, 400

    def put(self, placa):

        pass

    def delete(self, placa):

        pass