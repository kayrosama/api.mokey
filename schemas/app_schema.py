from pydantic import BaseModel, Field
from typing import Optional
from models.bdd_tables import RegGuia as RegModel

class RegGuiaAdd(BaseModel):
    idreg: Optional[int] = Field(default=None, ge=0)
    fecreg: Optional[str] = Field(default=None)
    fecmod: Optional[str] = Field(default=None)
    streg: Optional[int] = Field(default=None)
    stsrc: Optional[int] = Field(default=None)
    stpkg: Optional[int] = Field(default=None)
    stbox: Optional[int] = Field(default=None)
    idgui: int
    idemp: int
    fecguia: str
    guia: int
    snombres: str
    sapeuno: str
    sapedos: Optional[str] = Field(default=None)
    sapetres: Optional[str] = Field(default=None)
    spais: int
    steluno: int
    steldos: Optional[int] = Field(default=None)
    dnombres: str
    dapeuno: str
    dapedos: Optional[str] = Field(default=None)
    dapetres: Optional[str] = Field(default=None)
    dpais: int
    dteluno: int
    dteldos: Optional[int] = Field(default=None)
    ddiruno: Optional[str] = Field(default=None)
    ddirdos: Optional[str] = Field(default=None)
    destado: str
    dciudad: str
    dzipcode: Optional[int] = Field(default=None)
    idgrupo: int
    idregion: int
    monto: float
    peso: float
    productos: Optional[str] = Field(default=None)
    observaciones: Optional[str] = Field(default=None)

class RegGuiaFunctVal(BaseModel):
    guia: int
    snombres: str
    sapeuno: str
    steluno: int
    dnombres: str
    dapeuno: str
    dteluno: int

    def __init__(self, db) -> None:
        self.db = db
    
    def functval_id(self, id):
        result = self.db.query(RegModel).filter(RegModel.idreg == id).first()
        return result
       
    def functval_src(self, snombres: str, sapeuno: str, steluno: int):
        vcli_src = self.db.query(RegModel).filter(RegModel.steluno == int(steluno), 
                                                RegModel.snombres == str(snombres).upper().strip(), 
                                                RegModel.sapeuno == str(sapeuno).upper().strip()).first()
        return vcli_src
    
    def functval_dst(self, dnombres: str, dapeuno: str, dteluno: int):
        vcli_dst = self.db.query(RegModel).filter(RegModel.dteluno == int(dteluno), 
                                                RegModel.dnombres == str(dnombres).upper().strip(), 
                                                RegModel.dapeuno == str(dapeuno).upper().strip()).first()
        return vcli_dst
