from flask_restful import Resource, reqparse, ResponseBase
from model.servico import ServicoModel

argumentos = reqparse.RequestParser()
argumentos.add_argument('descricao', type=str, required=True, help="Campo 'descricao' não pode ser nulo.")
argumentos.add_argument('fkcodcarro', type=int, required=True, help="Campo 'fkcodcarro' não pode ser nulo.")
argumentos.add_argument('fkcodvalor', type=int, required=True, help="Campo 'fkcodvalor' não pode ser nulo.")
argumentos.add_argument('fkcodusuario', type=int, required=True, help="Campo 'fkcodusuario' não pode ser nulo.")
argumentos.add_argument('fkcodstatus', type=int, required=True, help="Campo 'fkcodstatus' não pode ser nulo.")

class Servicos(Resource):

    def get(self):

        lista_servicos = []
        servicos = ServicoModel.read_servicos()
        
        if servicos:

            for servico in servicos:
    
                lista_servicos.append(servico.json())

            return {'message': lista_servicos}, 200
            
        return {'message': 'Servicos não encontrados!'}, 404

    def post(self):

        dados = argumentos.parse_args()
        servico = ServicoModel(**dados)

        if servico.read_servico_before_post(servico.descricao):
            response = ResponseBase(response={'Servico já existe na base de dados!'}, 
                                    status=200, 
                                    headers={'location': '/servico/' + str(servico.read_servico_before_post(servico.descricao))})
            return response
        
        if servico.create_servico():
            response = ResponseBase(response={'Servico criado com sucesso!'}, 
                                    status=201, 
                                    headers={'location': '/servico/' + str(servico.pkcodservico)})
            return response

        else:
            response = ResponseBase(response={'Erro ao salvar Servico!'}, 
                                    status=500)
            return response

class Servico(Resource):

    def get(self, pkcodservico):
        
        servico = ServicoModel.read_servico(pkcodservico)

        if servico:
            return {'message': servico.json()}
            
        return {'message': 'Servico não encontrado!'}, 404

    def put(self, pkcodservico):

        dados = argumentos.parse_args()
        servico = ServicoModel.read_servico(pkcodservico)

        if servico:

            servico.update_servico(**dados)
            return {'message': 'Servico editado com sucesso!'}

        return {'message': 'Servico não encontrado!'}, 404

    def delete(self, pkcodservico):

        servico = ServicoModel.read_servico(pkcodservico)

        if servico:
            
            servico.delete_servico()
            return {'message': 'Servico deletado com sucesso!'}

        return {'message': 'Servico não encontrado!'}, 404