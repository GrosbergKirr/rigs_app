from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base


class Oil_rigs(Base):

    __tablename__ = 'oil_rigs'

    id = Column(Integer, primary_key=True)
    name = Column(String, comment="Наименование вышки")
    location = Column(Integer, ForeignKey("location.id"), comment="Расположение вышки")
    height = Column(Integer, comment="Высота вышки")
    diameter = Column(Integer, comment="Диаметр бурильной шахты")
    depth = Column(Integer, comment="Глубина бурения")
    drill_type = Column(Integer, ForeignKey("drill.id"), comment="Тип бурения")
    energy_type = Column(Integer, ForeignKey("energy.id"), comment="Тип энергопотребления")
    drill = relationship("Drill")
    energy = relationship("Energy")
    location_place = relationship("Location")




class Drill(Base):

    __tablename__ = 'drill'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    effectiveness = Column(String)


class Energy(Base):

    __tablename__ = 'energy'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    effectiveness = Column(String)


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    name = Column(String)

