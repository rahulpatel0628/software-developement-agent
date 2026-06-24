from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('postgresql://user:password@host:port/dbname')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db = Session()