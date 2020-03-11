from peewee import SqliteDatabase, Model, PrimaryKeyField, CharField

db = SqliteDatabase('wgpark.db')

class CarroDb(Model):

    pkcodcarro = PrimaryKeyField(null=False, primary_key=True)
    placa = CharField(null=False)
    modelo = CharField(null=False)
    
    class Meta:
        database = db
        table_name = 'TB_CarroModel'
    
