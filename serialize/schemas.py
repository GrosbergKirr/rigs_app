from pydantic import BaseModel, ConfigDict
from typing import Optional


class PyRigs(BaseModel):
    id: int
    name: str
    location: int
    height: int
    diameter: int
    depth: int
    drill_type: Optional[int] = None
    energy_type: Optional[int] = None



class PyUpdate_rigs(BaseModel):
    id: int
    name: Optional[str] = None
    location: Optional[int] = None
    height: Optional[int] = None
    diameter: Optional[int] = None
    depth: Optional[int] = None
    drill_type: Optional[int] = None
    energy_type: Optional[int] = None


class PyDel_rig(BaseModel):
    id: int