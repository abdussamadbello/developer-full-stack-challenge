
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from databases import Database


DATABASE_URL = "postgresql://abdussamadbinbello:jRb3Xr0vKNPI@ep-long-cake-674521.us-east-2.aws.neon.tech/neondb"
database = Database(DATABASE_URL)

metadata = MetaData()


engine = create_engine(
    DATABASE_URL
)

metadata.create_all(engine)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()