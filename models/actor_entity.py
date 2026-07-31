from sqlalchemy import Column, Integer, String
from database.database import Base

class ActorEntity(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)

    from models.actor_entity import ActorEntity

def create_tables():
    Base.metadata.create_all(bind=engine)