from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.actor import Actor
from models.user_entity import UserEntity
from interfaces.i_actor_repository import IActorRepository
from repositories.actor_db_repository import ActorDbRepository
from database.database import SessionLocal
from auth.auth import get_current_user

router = APIRouter(prefix="/actors", tags=["Actors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_repo(db: Session = Depends(get_db)) -> IActorRepository:
    return ActorDbRepository(db)

# Public - anyone can read
@router.get("/")
def get_all(repo: IActorRepository = Depends(get_repo)):
    return repo.get_all()

@router.get("/{id}")
def get_by_id(id: int, repo: IActorRepository = Depends(get_repo)):
    return repo.get_by_id(id)

# Protected - requires JWT token
@router.post("/")
def create(actor: Actor, repo: IActorRepository = Depends(get_repo), current_user: UserEntity = Depends(get_current_user)):
    return repo.create(actor)

@router.put("/{id}")
def update(id: int, actor: Actor, repo: IActorRepository = Depends(get_repo), current_user: UserEntity = Depends(get_current_user)):
    return repo.update(id, actor)

@router.delete("/{id}")
def delete(id: int, repo: IActorRepository = Depends(get_repo), current_user: UserEntity = Depends(get_current_user)):
    return repo.delete(id)