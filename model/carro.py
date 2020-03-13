
from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase

db = SqliteDatabase('wgpark.db')

class CarroModel(Model):

    pkcodcarro = PrimaryKeyField(null=False, primary_key=True)
    placa = CharField(null=False)
    modelo = CharField(null=False)
    
    class Meta:
        database = db
        table_name = 'TB_CarroModel'

    def create_carro(self):

        try:
            self.save()
            return {'message': 'carro criado com sucesso'}
        
        except Exception as erro:
            return {'message': str(erro)}
    
    @classmethod
    def read_carro(cls, placa):

        carro = cls.get_or_none(cls.placa == placa)
        if carro:
            return carro
            
        return None

    def update_carro(self, placa, modelo):

        self.placa = placa
        self.modelo = modelo

    def delete_carro(self):
        pass
     
    def json(self):

        return {
                'pkcodcarro': self.pkcodcarro,
                'placa': self.placa,
                'modelo': self.modelo
               }
