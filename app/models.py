from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Game(Base):
	__tablename__ = "games"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(200), nullable=False)
	platform = Column(String(50))
	genre = Column(String(50))
	release = Column(String(20))
	rating = Column(Float)
