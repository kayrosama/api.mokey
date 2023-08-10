from pydantic import BaseModel, Field
from typing import Optional

class RegGuia(BaseModel):
    idreg: Optional[int] = Field(default=None, ge=0)
    fecreg: Optional[str] = Field(default=None)
    fecmod: Optional[str] = Field(default=None)
    streg: int
    stsrc: int
    stpkg: int
    stbox: int
    idguia: int
    idemp: int
    emp_razon: Optional[str] = Field(default=None)
    fecguia: str
    guia: int
    snombres: str
    sapeuno: str
    sapedos: str
    sapetres: str
    spais: int
    steluno: int
    steldos: Optional[int] = Field(default=None)
    dnombres: str
    dapeuno: str
    dapedos: str
    dapetres: str
    dpais: int
    dteluno: int
    dteldos: Optional[int] = Field(default=None)
    ddiruno: Optional[str] = Field(default=None)
    ddirdos: Optional[str] = Field(default=None)
    destino: Optional[str] = Field(default=None)
    dciudad: Optional[str] = Field(default=None)
    dzipcode: Optional[int] = Field(default=None)
    idgrupo: Optional[int] = Field(default=None)
    idregion: Optional[int] = Field(default=None)
    monto: float
    peso: float
    productos: str
    observaciones: str
    