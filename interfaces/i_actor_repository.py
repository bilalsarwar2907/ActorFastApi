from abc import ABC, abstractmethod
from models.actor import Actor

class IActorRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Actor]: pass

    @abstractmethod
    def get_by_id(self, id: int) -> Actor | None: pass

    @abstractmethod
    def create(self, actor: Actor) -> Actor: pass

    @abstractmethod
    def delete(self, id: int) -> bool: pass

    @abstractmethod
    def update(self, id: int, actor: Actor) -> Actor: pass

    @abstractmethod
    def update(self, id: int, actor: Actor) -> Actor | None: pass