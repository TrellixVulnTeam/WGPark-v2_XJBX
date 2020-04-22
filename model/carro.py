
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
            return True
        
        except:
            return None
    
    @classmethod
    def read_carros(cls):

        carros = cls.select()
        if carros:
            return carros
            
        return None

    @classmethod
    def read_carro(cls, placa):

        carro = cls.get_or_none(cls.placa == placa)
        if carro:
            return carro
            
        return None

    def update_carro(self, placa, modelo):

        try:
            self.placa = placa
            self.modelo = modelo
        except:
            return None
            
    def delete_carro(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {
                'pkcodcarro': self.pkcodcarro,
                'placa': self.placa,
                'modelo': self.modelo
               }