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
    idgui: int
    idemp: int
    emp_razon: Optional[str] = Field(default=None)
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
    destado: Optional[str] = Field(default=None)
    dciudad: Optional[str] = Field(default=None)
    dzipcode: Optional[int] = Field(default=None)
    idgrupo: Optional[int] = Field(default=None)
    idregion: Optional[int] = Field(default=None)
    monto: float
    peso: float
    productos: Optional[str] = Field(default=None)
    observaciones: Optional[str] = Field(default=None)

class RegGuiaInsert(BaseModel):
    idreg: Optional[int] = Field(default=None)
    fecreg: Optional[str] = Field(default=None)
    fecmod: Optional[str] = Field(default=None)
    streg: int
    stsrc: int
    stpkg: int
    stbox: int
    idgui: int
    idemp: int
    emp_razon: Optional[str] = Field(default=None)
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
    destado: Optional[str] = Field(default=None)
    dciudad: Optional[str] = Field(default=None)
    dzipcode: Optional[int] = Field(default=None)
    idgrupo: Optional[int] = Field(default=None)
    idregion: Optional[int] = Field(default=None)
    monto: float
    peso: float
    productos: Optional[str] = Field(default=None)
    observaciones: Optional[str] = Field(default=None)