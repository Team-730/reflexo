from puzzle_generator import get_puzzle
from database import DataBase as DB

db = DB()
get_puzzle(db.getMatrix())