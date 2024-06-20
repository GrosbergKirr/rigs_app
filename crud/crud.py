import http

from fastapi import HTTPException

from models.database import Session
from models.models import Oil_rigs, Location
from serialize.schemas import *




class CRUD:

    @classmethod
    def insert(cls, rig: PyRigs):
        session = Session()
        rg_map = rig.model_dump()
        inserted_rig = Oil_rigs(**rg_map)
        session.add(inserted_rig)
        session.commit()
        return "Success"


    @classmethod
    def select(cls):
        session = Session()
        return session.query(Oil_rigs).all()

    @classmethod
    def update(cls, rig_update: PyUpdate_rigs):
        session = Session()
        rig_id = session.query(Oil_rigs).filter(Oil_rigs.id == rig_update.id).first()
        if not rig_id.id:
            raise HTTPException(status_code=404, detail="Rig_id not found")

        if rig_update.name is not None:
            rig_id.name = rig_update.name
        if rig_update.location is not None:
            rig_id.location = rig_update.location
        if rig_update.height is not None:
            rig_id.height = rig_update.height
        if rig_update.diameter is not None:
            rig_id.diameter = rig_update.diameter
        if rig_update.depth is not None:
            rig_id.depth = rig_update.depth
        if rig_update.drill_type is not None:
            rig_id.drill_type = rig_update.drill_type
        if rig_update.energy_type is not None:
            rig_id.energy_type = rig_update.energy_type

        session.commit()
        return f"Rig {rig_id.id} updated successfully",

    @classmethod
    def delete(cls, del_rig: PyDel_rig):
        session = Session()
        rig_id = session.query(Oil_rigs).filter(Oil_rigs.id == del_rig.id).first()
        session.delete(rig_id)
        session.commit()
        return f"Rig {rig_id.id} deleted successfully"

    @classmethod
    def sidetableinsert(cls):
        session = Session()
        for i in range(1, 4):
            existing_loc = session.query(Location).filter_by(id=i).first()
            if existing_loc is None:
                inserted_loc = Location(**{"id": i, "name": f"loc{i}"})
                inserted_drill = Location(**{"id": i, "name": f"loc{i}"})
                inserted_en = Location(**{"id": i, "name": f"loc{i}"})
                session.add(inserted_loc)
                session.add(inserted_drill)
                session.add(inserted_en)
                session.commit()
            else:
                break