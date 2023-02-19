"""
imports
"""
import psycopg2
from os import path as os_path
from configparser import ConfigParser
from .interfaces import DatabaseAccess

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
        # create a parser
        parser = ConfigParser()

        # get path to config file
        base_dir = os_path.dirname(os_path.dirname(os_path.abspath(__file__)))
        filename = base_dir+filename
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db


    # this funktion connects to the postgres database and returns ist version
    def get_version(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            params = self.config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database ...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
            
            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def get_connection(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        cur = None
        try:
            # read connection parameters
            params = self.config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database ...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return conn, cur


    def close_connection(self, conn, cursor):
        try:
            print('Closing database connecting...')
            conn.commit()
            # close the communication with the PostgreSQL
            cursor.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)



    """-------------------------extern--------------------------"""
    def add_account(self, player_id, username, password, age, is_admin):
        try:
            conn, cursor = self.get_connection()
            print("Add Player: {0}, {1}, {2}, {3}, {4}".format(player_id, username, password, age, is_admin))
            # execure statment
            sql = "INSERT INTO player(player_id, username, password, age, is_admin) VALUES(%s, %s, %s, %s, %s);"
            cursor.execute(sql, (player_id, username, password, age, is_admin,))
            # execure statment))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def update_account(self, player_id, username, password, age, is_admin):
        try:
            conn, cursor = self.get_connection()
            print("Update Player: {0} with {1}, {2}, {3}, {4}".format(player_id, username, password, age, is_admin))
            # execure statment
            sql = "UPDATE player SET username = %s, password = %s, age = %s, is_admin = %s WHERE player_id = %s;"
            cursor.execute(sql, (username, password, age, is_admin, player_id,))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    
    def delete_account(self, player_id):
        try:
            conn, cursor = self.get_connection()
            print("Delete Player: {0}".format(player_id))
            # execure statment
            sql = "DELETE FROM player WHERE player_id = %s;"
            cursor.execute(sql, (player_id,))
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    #
    def get_player_table(self):
        try:
            conn, cursor = self.get_connection()
            print("Player Datatable:")
            players = []
            # execure statment
            cursor.execute('SELECT * FROM player')
            for entry in cursor:
                players.append(entry)
            self.close_connection(conn, cursor)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return players


    def get_player(self, player_id):
        try:
            conn, cursor = self.get_connection()
            print("Player with ID: {0}".format(player_id))
            player = 0
            # execure statment
            sql = "SELECT * FROM player WHERE player_id = %s;"
            cursor.execute(sql, (player_id,))
            player = cursor.fetchone()
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return player


    def get_game_table(self):
        try:
            conn, cursor = self.get_connection()
            print("Game Datatable:")
            games = []
            # execure statment
            cursor.execute('SELECT * FROM game')
            for entry in cursor:
                games.append(entry)
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return games


    def get_game(self, game_name):
        try:
            conn, cursor = self.get_connection()
            print("Game with Name: {0}".format(game_name))
            game = 0
            # execure statment
            sql = "SELECT * FROM game WHERE game = %s;"
            cursor.execute(sql, (game_name,))
            game = cursor.fetchone()
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return game


    def get_game_stat_table(self):
        try:
            conn, cursor = self.get_connection()
            print("Game Statistic Datatable:")
            game_stats = []
            # execure statment
            cursor.execute('SELECT * FROM gamestats')
            for entry in cursor:
                game_stats.append(entry)
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return game_stats


    def get_game_stat(self, player_id, game_id):
        try:
            conn, cursor = self.get_connection()
            print("Statistic of game {0} from player: {1}".format(game_id, player_id))
            player_game_stats = 0
            # execure statment
            sql = "SELECT * FROM gamestats WHERE player_id = %s AND game_id = %s;"
            cursor.execute(sql, (player_id, game_id,))
            player_game_stats = cursor.fetchone()
            self.close_connection(conn, cursor)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return player_game_stats

if __name__ == "__main__":
    pass
