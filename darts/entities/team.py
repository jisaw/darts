from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Team(Base):

	__tablename__ = "teams"

	id = Column(Integer, primary_key = True)
	gameId = Column(Integer)

	def __init__(self, gameId):
		self.gameId = gameId
