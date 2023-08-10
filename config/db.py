from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "mysql+pymysql://root:admin123@localhost/kdb"
engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()