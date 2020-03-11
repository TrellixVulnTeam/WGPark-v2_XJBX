
#from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase
from database.carro import CarroDb
#db = SqliteDatabase('wgpark.db')

class CarroModel(CarroDb):

    def create_carro(self):

        try:
            self.save()
            return {'message': 'carro criado com sucesso'}
        
        except Exception as erro:
            return {'message': str(erro)}
    
    @classmethod
    def read_carro(cls, placa):

        try:
            carro = cls.select().where(cls.placa == placa).limit(1).get()
            return carro

        except:
            
            return None

    def update_carro(self):
        pass

    def delete_carro(self):
        pass
     
    def json(self):

        return {
                'pkcodcarro': self.pkcodcarro,
                'placa': self.placa,
                'modelo': self.modelo
               }
