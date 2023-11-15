from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

bdd_url = "mysql+pymysql://kohana:Kinteki#69@localhost/kdb"
engine = create_engine(bdd_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()