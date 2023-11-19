from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from config.bdd import Session
from models.bdd_tables import RegGuia as RegModel
from services.app_service import RegService
from schemas.app_schema import RegGuiaAdd, RegGuiaGetGuia

reg_router = APIRouter()


@reg_router.get('/reg', tags=['records'], response_model=List[RegGuiaGetGuia], status_code=200)
def get_reg_guia() -> List[RegGuiaGetGuia]:
    db = Session()
    result = RegService(db).get_reg_guia()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@reg_router.post('/reg', tags=['records'], response_model=dict, status_code=201)
def add_reg(reg: RegGuiaAdd) -> dict:
    db = Session()
    RegService(db).add_reg(reg)
    return JSONResponse(status_code=201, content={"message": "Se ha hecho el registro."})

@reg_router.delete('/reg/{id}', tags=['records'], response_model=dict, status_code=200)
def del_reg(id: int) -> dict:
    db = Session()
    result = RegService(db).get_reg(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    RegService(db).del_reg(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro."})