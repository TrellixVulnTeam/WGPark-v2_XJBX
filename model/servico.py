
from peewee import PrimaryKeyField, CharField, ForeignKeyField, Model, SqliteDatabase
from model.carro import CarroModel
from model.valor import ValorModel
from model.usuario import UsuarioModel
from model.status import StatusModel

db = SqliteDatabase('wgpark.db', pragmas={'foreign_keys': 1})

class ServicoModel(Model):

    pkcodservico = PrimaryKeyField(null=False, primary_key=True)
    descricao = CharField(null=False, unique=True)
    fkcodcarro = ForeignKeyField(CarroModel, null=False)
    fkcodvalor = ForeignKeyField(ValorModel, null=False)
    fkcodusuario = ForeignKeyField(UsuarioModel, null=False)
    fkcodstatus = ForeignKeyField(StatusModel, null=False)

    class Meta:
        database = db
        table_name = 'TB_ServicoModel'

    def create_servico(self):

        try:    
            self.save(force_insert=True)
            return True
        
        except:
            return None

    @classmethod
    def read_servicos(cls):

        servicos = cls.select()
        if servicos:
            return servicos
            
        return None

    @classmethod
    def read_servico_before_post(cls, descricao):

        servico = cls.get_or_none(cls.descricao == descricao)
        if servico:
            return servico
            
        return None

    @classmethod
    def read_servico(cls, pkcodservico):

        servico = cls.get_or_none(cls.pkcodservico == pkcodservico)
        if servico:
            return servico
            
        return None

    def update_servico(self, descricao, fkcodcarro, fkcodvalor, fkcodusuario, fkcodstatus):

        try:
            self.descricao = descricao
            self.fkcodcarro = fkcodcarro
            self.fkcodvalor = fkcodvalor
            self.fkcodusuario = fkcodusuario
            self.fkcodstatus = fkcodstatus
            self.save()
        except:
            return None
            
    def delete_servico(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {'pkcodservico': self.pkcodservico,
                'descricao': self.descricao,
                'fkcodcarro': self.fkcodcarro.pkcodcarro,
                'fkcodvalor': self.fkcodvalor.pkcodvalor,
                'fkcodusuario': self.fkcodusuario.pkcodusuario,
                'fkcodstatus': self.fkcodstatus.pkcodstatus
               }