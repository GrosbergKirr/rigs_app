import http
from typing import Annotated

import exceptiongroup
from fastapi import APIRouter, Depends
from models.database import Session
from crud.crud import CRUD
from serialize.schemas import *
import pandas as pd


router = APIRouter(
    prefix="/Rigs",
    tags=["Petroleum"],
)


@router.post("/create")
def Create_rig(
    rig: Annotated[PyRigs, Depends()]
):
    res = CRUD.insert(rig)
    return http.HTTPStatus.OK, res

@router.get("/get_all")
def Get_all():
    res = CRUD.select()
    l = []
    for i in res:
        l.append({"id": i.id, "name": i.name, "location": i.location, "height": i.height, "diameter ": i.diameter,
                  "depth ": i.depth, "drill_type ": i.drill_type, "energy_type": i.energy_type})

    df = pd.DataFrame(l)

    df.to_excel("./data/all_rigs.xlsx", index=True)
    print(df)
    return http.HTTPStatus.OK, res


@router.post("/update_rig")
def Update_rig(
    rig: Annotated[PyUpdate_rigs, Depends()]
):
    res = CRUD.update(rig)
    return http.HTTPStatus.OK, res

@router.post("/del_rig")
def Del_rig(
    rig: Annotated[PyDel_rig, Depends()]
):
    res = CRUD.delete(rig)
    return http.HTTPStatus.OK, res