from fastapi import APIRouter, Depends
from models.actor import Actor
from interfaces.i_actor_repository import IActorRepository
from repositories.actor_repository import ActorRepository

router = APIRouter(prefix="/actors", tags=["Actors"])

def get_repo() -> IActorRepository:
    return ActorRepository()

@router.get("/")
def get_all(repo: IActorRepository = Depends(get_repo)):
    return repo.get_all()

@router.get("/{id}")
def get_by_id(id: int, repo: IActorRepository = Depends(get_repo)):
    return repo.get_by_id(id)

@router.post("/")
def create(actor: Actor, repo: IActorRepository = Depends(get_repo)):
    return repo.create(actor)

@router.delete("/{id}")
def delete(id: int, repo: IActorRepository = Depends(get_repo)):
    return repo.delete(id)

