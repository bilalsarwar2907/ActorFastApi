from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.actor import Actor
from interfaces.i_actor_repository import IActorRepository
from repositories.actor_db_repository import ActorDbRepository
from database.database import SessionLocal

router = APIRouter(prefix="/actors", tags=["Actors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_repo(db: Session = Depends(get_db)) -> IActorRepository:
    return ActorDbRepository(db)

@router.get("/")
def get_all(repo: IActorRepository = Depends(get_repo)):
    return repo.get_all()

@router.get("/{id}")
def get_by_id(id: int, repo: IActorRepository = Depends(get_repo)):
    return repo.get_by_id(id)

@router.post("/")
def create(actor: Actor, repo: IActorRepository = Depends(get_repo)):
    return repo.create(actor)

@router.put("/{id}")
def update(id: int, actor: Actor, repo: IActorRepository = Depends(get_repo)):
    return repo.update(id, actor)

@router.delete("/{id}")
def delete(id: int, repo: IActorRepository = Depends(get_repo)):
    return repo.delete(id)