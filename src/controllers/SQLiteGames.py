from models.SQliteGames import SQLiteGameModel
class SQLiteGamesController:
   def get_games():
      return SQLiteGameModel.get_games()
   
   
