from interfaces.i_actor_repository import IActorRepository
from models.actor import Actor

class ActorRepository(IActorRepository):

    def __init__(self):
        self._actors: list[Actor] = []

    def get_all(self):
        return self._actors

    def get_by_id(self, id):
        return next((a for a in self._actors if a.id == id), None)

    def create(self, actor):
        self._actors.append(actor)
        return actor

    def update(self, id, actor):
        for i, a in enumerate(self._actors):
            if a.id == id:
                self._actors[i] = actor
                return actor
        return None

    def delete(self, id):
        for i, a in enumerate(self._actors):
            if a.id == id:
                del self._actors[i]
                return True
        return False