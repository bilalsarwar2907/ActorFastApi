from sqlalchemy.orm import Session
from interfaces.i_actor_repository import IActorRepository
from models.actor import Actor
from models.actor_entity import ActorEntity

class ActorDbRepository(IActorRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(ActorEntity).all()

    def get_by_id(self, id):
        return self.db.query(ActorEntity).filter(ActorEntity.id == id).first()

    def create(self, actor: Actor):
        entity = ActorEntity(id=actor.id, name=actor.name, age=actor.age)
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, id, actor: Actor):
        entity = self.db.query(ActorEntity).filter(ActorEntity.id == id).first()
        if entity:
            entity.name = actor.name
            entity.age = actor.age
            self.db.commit()
            self.db.refresh(entity)
        return entity

    def delete(self, id):
        entity = self.db.query(ActorEntity).filter(ActorEntity.id == id).first()
        if entity:
            self.db.delete(entity)
            self.db.commit()
            return True
        return False