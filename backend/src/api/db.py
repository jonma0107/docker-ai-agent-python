import os
from sqlmodel import Session, SQLModel, create_engine

# Obtener la variable de entorno
DATABASE_URL = os.environ.get("DATABASE_URL")

# Validar que esté definida
if not DATABASE_URL:
    raise NotImplementedError("`DATABASE_URL` is not set.")

# Reemplazo de protocolo por compatibilidad (solo si viene con postgres://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)

# Crear el engine
engine = create_engine(DATABASE_URL, echo=True)

# Inicializa las tablas definidas con SQLModel
def init_db():
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)

# Usar sesión en endpoints
def get_session():
    with Session(engine) as session:
        yield session
