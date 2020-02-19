from flask_restful import Resource, reqparse
from model.carro import CarroModel

class CarroController(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('pkcodcarro', type=str, required=True, help="Campo 'pkcodcarro' não pode ser nulo.")
    argumentos.add_argument('placa', type=str, required=True, help="Campo 'placa' não pode ser nulo.")
    argumentos.add_argument('modelo', type=str, required=True, help="Campo 'modelo' não pode ser nulo.")

    def get(self):
        
        carro = CarroModel.read_carro()

        if carro:
            return {'message': carro.json()}

    def post(self):

        try:

            dados = CarroController.argumentos.parse_args()
            carro = CarroModel(**dados)
            carro.create_carro()

            return {'message': carro.json()}
        
        except Exception as erro:
            
            return {'message': str(erro)}, 400

    def put(self):

        pass

    def delete(self):

        pass