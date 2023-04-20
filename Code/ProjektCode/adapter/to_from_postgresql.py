"""
imports
"""
import psycopg2
from os import path as os_path
from configparser import ConfigParser
from .interfaces import DatabaseAccess


# this class handles inteactions between the python code and the postgres database
class PostgreSqlAdapter(DatabaseAccess):
    """
    global variables
    """
    def __init__(self):
        pass

    """
    functions
    """
    """-------------------------intern--------------------------"""
    # this funktion takes the database settings from a .ini file and returns them as list
    def config(self, filename='\docker\docker_postgresql\player_db.ini', section='postgresql'):
        parser = ConfigParser()
        base_dir = os_path.dirname(os_path.dirname(os_path.abspath(__file__)))
        filename = base_dir+filename
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]

        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db


    # this funktion creates a connection to the database
    # returns the connection and cursor object
    def get_connection(self):
        conn = None
        cur = None
        try:
            params = self.config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return conn, cur


    # this funktion saves the changes made to the database during the connection
    # - takes a connection objekt
    def commit_action(self, conn):
        try:
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    # this funktion ...
    def close_connection(self, conn, cursor):
        try:
            self.commit_action(conn)
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)



    """-------------------------extern--------------------------"""
    # this funktion ...
    def add_account(self, username, password, age, is_admin):
        try:
            conn, cursor = self.get_connection()
            sql = "INSERT INTO player(username, password, age, is_admin) VALUES(%s, %s, %s, %s);"
            cursor.execute(sql, (username, password, age, is_admin,))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        

    # this funktion ...
    def add_account_gamestats(self, player_id):
        try:
            conn, cursor = self.get_connection()
            sql = "SELECT count(game_id) FROM game;"
            cursor.execute(sql, (player_id,))
            game_count = cursor.fetchone()[0]
            for game_id in range(1,game_count+1):
                sql = "INSERT INTO gamestats(fk_player_id, fk_game_id, wins, losses) VALUES(%s, %s, %s, %s);"
                cursor.execute(sql, (player_id, game_id, 0, 0))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)    

    
    # this funktion ...
    def last_added_account(self):
        id_of_added_account = -1
        try:
            conn, cursor = self.get_connection()
            cursor.execute('SELECT MAX(player_id) FROM player')
            id_of_added_account = cursor.fetchone()[0]
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return id_of_added_account


    # this funktion ...
    def update_account(self, player_id, username, password, age, is_admin):
        try:
            conn, cursor = self.get_connection()
            sql = "UPDATE player SET username = %s, password = %s, age = %s, is_admin = %s WHERE player_id = %s;"
            cursor.execute(sql, (username, password, age, is_admin, player_id,))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    
    # this funktion ...
    def delete_account(self, player_id):
        try:
            conn, cursor = self.get_connection()
            sql = "DELETE FROM player WHERE player_id = %s;"
            cursor.execute(sql, (player_id,))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    # this funktion ...
    def delete_gamestats(self, player_id):
        try:
            conn, cursor = self.get_connection()
            sql = "DELETE FROM gamestats WHERE fk_player_id = %s;"
            cursor.execute(sql, (player_id,))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    
    # this funktion ...
    def get_player_table(self):
        try:
            conn, cursor = self.get_connection()
            players = []
            cursor.execute('SELECT * FROM player')
            for entry in cursor:
                players.append(entry)
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return players


    # this funktion ...
    def get_player(self, player_id):
        try:
            conn, cursor = self.get_connection()
            player = 0
            sql = "SELECT * FROM player WHERE player_id = %s;"
            cursor.execute(sql, (player_id,))
            player = cursor.fetchone()
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return player


    # this funktion ...
    def get_game_table(self):
        try:
            conn, cursor = self.get_connection()
            games = []
            cursor.execute('SELECT * FROM game')
            for entry in cursor:
                games.append(entry)
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return games


    # this funktion ...
    def get_game(self, game_name):
        try:
            conn, cursor = self.get_connection()
            game = 0
            sql = "SELECT * FROM game WHERE game = %s;"
            cursor.execute(sql, (game_name,))
            game = cursor.fetchone()
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return game


    # this funktion ...
    def get_game_stat_table(self):
        try:
            conn, cursor = self.get_connection()
            game_stats = []
            cursor.execute('SELECT * FROM gamestats')
            for entry in cursor:
                game_stats.append(entry)
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return game_stats


    # this funktion ...
    def get_game_stat(self, player_id, game_id):
        try:
            conn, cursor = self.get_connection()
            player_game_stats = 0
            sql = "SELECT * FROM gamestats WHERE fk_player_id = %s AND fk_game_id = %s;"
            cursor.execute(sql, (player_id, game_id,))
            player_game_stats = cursor.fetchone()
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return player_game_stats


    # this funktion ...
    def add_win(self, player_id, game_id):
        try:
            conn, cursor = self.get_connection()
            sql = "UPDATE gamestats SET wins = wins +1 WHERE fk_player_id = %s AND fk_game_id = %s;"
            cursor.execute(sql, (player_id, game_id,))
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    # this funktion ...
    def add_loss(self, player_id, game_id):
        try:
            conn, cursor = self.get_connection()
            sql = "UPDATE gamestats SET losses = losses +1 WHERE fk_player_id = %s AND fk_game_id = %s;"
            cursor.execute(sql, (player_id, game_id,))
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


if __name__ == "__main__":
    print("The PostgreSqlAdapter handles inteactions between the python code and the postgres database")
