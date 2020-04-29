
from peewee import PrimaryKeyField, CharField, ForeignKeyField, Model, SqliteDatabase, Check
from model.tipo_usuario import TipoUsuarioModel
db = SqliteDatabase('wgpark.db', pragmas={'foreign_keys': 1})

class UsuarioModel(Model):

    pkcodusuario = PrimaryKeyField(null=False, primary_key=True)
    nome = CharField(null=False)
    cpf = CharField(null=False, unique=True)
    fkcodtipousuario = ForeignKeyField(TipoUsuarioModel, null=False)

    class Meta:
        database = db
        table_name = 'TB_UsuarioModel'

    def create_usuario(self):

        try:    
            self.save(force_insert=True)
            return True
        
        except:
            return None

    @classmethod
    def read_usuarios(cls):

        usuarios = cls.select()
        if usuarios:
            return usuarios
            
        return None

    @classmethod
    def read_usuario(cls, pkcodvalor):

        usuario = cls.get_or_none(cls.pkcodvalor == pkcodvalor)
        if usuario:
            return usuario
            
        return None

    def update_usuario(self, nome, cpf, fkcodtipousuario):

        try:
            self.nome = nome
            self.cpf = cpf
            self.fkcodtipousuario = fkcodtipousuario
            self.save()
        except:
            return None
            
    def delete_usuario(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {
                'pkcodusuario': self.pkcodusuario,
                'nome': self.nome,
                'cpf': self.cpf,
                'fkcodtipousuario': self.fkcodtipousuario.pkcodtipo
               }