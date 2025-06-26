SQLITE = "sqlite:///proyect.db"
POSTGRESQL = "postgresql+psycopg2://postgres:Sistemas1*@localhost:5432/blogposts_db"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = POSTGRESQL