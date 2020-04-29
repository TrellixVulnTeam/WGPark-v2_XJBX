
from peewee import PrimaryKeyField, CharField, FloatField, Model, SqliteDatabase

db = SqliteDatabase('wgpark.db')

class ValorModel(Model):

    pkcodvalor = PrimaryKeyField(null=False, primary_key=True)
    descricao = CharField(null=False, unique=True)
    valor = FloatField(null=False)
    
    class Meta:
        database = db
        table_name = 'TB_ValorModel'

    def create_valor(self):

        try:
            self.save(force_insert=True)
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
    def read_valor_before_post(cls, descricao):

        valor = cls.get_or_none(cls.descricao == descricao)
        if valor:
            return valor
            
        return None

    @classmethod
    def read_valor(cls, pkcodvalor):

        valor = cls.get_or_none(cls.pkcodvalor == pkcodvalor)
        if valor:
            return valor
            
        return None

    def update_valor(self, descricao, valor):

        try:
            self.descricao = descricao
            self.valor = valor
            self.save()
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
