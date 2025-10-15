

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:Elektroniker.1969@localhost:3306/bookshop', echo=True)

# Optional: SessionLocal pentru sesiuni DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


