from flask_restful import Resource, reqparse, ResponseBase
from model.status import StatusModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('status', type=str, required=True, help="'Status' não pode ser nulo.")

class StatusList(Resource):

    def get(self):

        status_list = []
        status = StatusModel.read_status_list()

        if status:

            for s in status:
                status_list.append(s.json())

            return {'message': status_list}, 200
            
        return {'message': 'StatusList nao encontrados!'}, 404

    def post(self):

        dados = argumentos.parse_args()
        status = StatusModel(**dados)
        status.status = status.status.upper()

        if status.read_status(status.status):

            response = ResponseBase(response={'Status já existe na base de dados!'}, 
                                    status=200, 
                                    headers={'location': '/status/'+ status.status})
            return response
        
        if status.create_status():
            response = ResponseBase(response={'Status criado com sucesso!'}, 
                                    status=201, 
                                    headers={'location': '/status/'+ status.status})
            return response

        else:
            response = ResponseBase(response={'Erro ao salvar Status!'}, 
                                    status=500)
            return response

class Status(Resource):

    def get(self, status):
        
        status = StatusModel.read_status(status.upper())

        if status:
            return {'message': status.json()}
        
        return {'message': 'Status não encontrado!'}, 404

    def delete(self, status):

        status = StatusModel.read_status(status.upper())

        if status:
            status.delete_status()
            return {'message': 'Status deletado com sucesso!'}

        return {'message': 'Status não encontrado!'}, 404
