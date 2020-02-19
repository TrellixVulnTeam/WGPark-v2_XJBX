from database.carro import CarroDb

class CarroModel(CarroDb):
    
    def create_carro(self):

        try:
            CarroModel.create()
        
        except Exception as erro:
            return {'message': str(erro)}
    
    @classmethod
    def read_carro(cls):

        carro = cls.get_by_id(3)
        if carro:
            return carro

        return None

    def update_carro(self):
        pass

    def delete_carro(self):
        pass
     
    def json(self):
        return {
                'pkcodcarro': self.pkcodcarro,
                'placa': self.placa,
                'modelo': self.modelo
               }
