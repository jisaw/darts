from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

class Game(Base):

	__tablename__ = "games"

	id = Column(Integer, primary_key = True)
	players = Column(Integer)
	game = Column(Integer)
	round = Column(Integer)
	ready = Column(Integer)
	turn = Column(Integer)
	complete = Column(Integer)
	createdAt = Column(DateTime)

	def __init__(self, players, game, round, ready, complete, createdAt):
		self.players = players
		self.game = game
		self.round = round
		self.ready = ready
		self.complete = complete
		self.createdAt = createdAt
