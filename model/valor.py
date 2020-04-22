
from peewee import PrimaryKeyField, CharField, FloatField, Model, SqliteDatabase

db = SqliteDatabase('wgpark.db')

class ValorModel(Model):

    pkcodvalor = PrimaryKeyField(null=False, primary_key=True)
    descricao = CharField(null=False)
    valor = FloatField(null=False)
    
    class Meta:
        database = db
        table_name = 'TB_ValorModel'

    def create_valor(self):

        try:
            self.save()
            return True
        
        except:
            return None
    
    @classmethod
    def read_valores(cls):

        valores = cls.select()
        if valores:
            return valores
            
        return None

    @classmethod
    def read_valor(cls, descricao):

        valor = cls.get_or_none(cls.descricao == descricao)
        if valor:
            return valor
            
        return None

    def update_valor(self, descricao, valor):

        try:
            self.descricao = descricao
            self.valor = valor
        except:
            return None
            
    def delete_valor(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {
                'pkcodvalor': self.pkcodvalor,
                'descricao': self.descricao,
                'valor': self.valor
               }
