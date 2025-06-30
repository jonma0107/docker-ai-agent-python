import os
from sqlmodel import create_engine, Session, SQLModel

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    print("Initializing database...")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session



