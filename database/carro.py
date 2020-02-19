from peewee import SqliteDatabase, Model, IntegerField, CharField

db = SqliteDatabase('wgpark.db')


class BaseModel(Model):

    class Meta:
        database = db

class CarroDb(BaseModel):

    pkcodcarro = IntegerField(null=False, primary_key=True)
    placa = CharField(null=False)
    modelo = CharField(null=False)