from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database address
POSTGRES_DATABASE_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/fastapidb"

# create new engine postgresql
engine = create_engine(POSTGRES_DATABASE_URL)

# create session factory using the engine
session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)

base = declarative_base()

# create dependecy function to provide a database session to routes
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
