from pydantic import BaseModel, Field
from typing import Optional

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

class RegGuiaGetGuia(BaseModel):
    guia: int
    
class RegGuiaGetEnvia(BaseModel):
    snombres: str
    sapeuno: str
    spais: int

class RegGuiaGetRecibe(BaseModel):
    dnombres: str
    dapeuno: str
    dpais: int
