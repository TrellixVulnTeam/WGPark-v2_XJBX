
from peewee import PrimaryKeyField, CharField, FloatField, Model, SqliteDatabase

db = SqliteDatabase('wgpark.db')

class TipoUsuarioModel(Model):

    pkcodtipo = PrimaryKeyField(null=False, primary_key=True)
    descricao = CharField(null=False)
    
    class Meta:
        database = db
        table_name = 'TB_TipoUsuarioModel'

    def create_tipo(self):

        try:
            self.save()
        
        except Exception as erro:
            return {'message': str(erro)}
    
    @classmethod
    def read_tipos(cls):

        tipos = cls.select()
        if tipos:
            return tipos
            
        return None

    @classmethod
    def read_tipo(cls, descricao):

        tipo_usuario = cls.get_or_none(cls.descricao == descricao)
        if tipo_usuario:
            return tipo_usuario
            
        return None

    def update_tipo(self, descricao):

        try:
            self.descricao = descricao
        except:
            return None
            
    def delete_tipo(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {
                'pkcodtipo': self.pkcodtipo,
                'descricao': self.descricao
               }
