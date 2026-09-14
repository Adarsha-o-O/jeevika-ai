import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Local development fallback:
# If DATABASE_URL is not provided, Jeevika AI continues using SQLite.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./jeevika.db"
)


# SQLite requires a special connection option.
# PostgreSQL / Neon does not.
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
