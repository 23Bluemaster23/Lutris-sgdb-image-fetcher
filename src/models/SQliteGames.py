import sqlite3


con = sqlite3.connect("/home/bluedev/.local/share/lutris/pga.db")

class SQLiteGameModel():
    @staticmethod
    def get_games()->list[dict]:
        game_list:list[dict] = []
        res = con.execute('SELECT name,platform,slug FROM games').fetchall()
        for item in res:
            game = {}
            game['name'] = item[0]
            game['platform'] = item[1]
            game['slug'] = item[2]
            game_list.append(game)
        return game_list
