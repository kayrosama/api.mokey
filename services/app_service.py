from models.bdd_tables import RegGuia as RegModel
from schemas.app_schema import RegGuiaAdd
        
class RegService():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_reg_guia(self):
        result = self.db.query(RegModel).all()
        return result
    
    def get_reg(self, id):
        result = self.db.query(RegModel).filter(RegModel.idreg == id).first()
        return result
    
    def add_reg(self, reg: RegGuiaAdd):
        new_reg = RegModel(**reg.dict())
        self.db.add(new_reg)
        self.db.commit()
        return
    
    def del_reg(self, id):
        result = self.db.query(RegModel).filter(RegModel.idreg == id).first()
        self.db.delete(result)
        self.db.commit()
        return