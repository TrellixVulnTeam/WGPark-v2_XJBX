
from peewee import PrimaryKeyField, CharField, Model, SqliteDatabase, Check

db = SqliteDatabase('wgpark.db')

class StatusModel(Model):

    pkcodstatus = PrimaryKeyField(null=False, primary_key=True)
    status = CharField(null=False, constraints=[Check("status = 'O' or status = 'C'")])
    
    class Meta:
        database = db
        table_name = 'TB_StatusModel'
        constraints=[Check("status = upper('o') OR status = upper('c')")]

    def create_status(self):

        try:
            self.save(force_insert=True)
            return True

        except:
            return None
    
    @classmethod
    def read_status_list(cls):

        status = cls.select()
        
        if status:
            return status
            
        return None

    @classmethod
    def read_status(cls, status):

        status = cls.get_or_none(cls.status == status)

        if status:
            return status
            
        return None
            
    def delete_status(self):
        
        try:
            self.delete_instance()
        except:
            return None
     
    def json(self):

        return {
                'pkcodstatus': self.pkcodstatus,
                'status': self.status
               }
