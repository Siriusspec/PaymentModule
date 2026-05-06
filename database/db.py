from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
import os


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")


if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


if "sqlite" in DATABASE_URL:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
