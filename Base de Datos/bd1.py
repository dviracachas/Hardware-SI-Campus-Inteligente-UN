import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    # database = r""

    sql_create_general_table = """ CREATE TABLE IF NOT EXISTS general (
                                        cedula integer unique,
                                        TypeUser integer,
                                        ID_User integer unique
                                    ); """

    sql_create_bicicletas_table = """CREATE TABLE IF NOT EXISTS Bicicletas (
                                    cedula integer unique,
                                    TypeUser integer,
                                    ID_User integer unique,
                                    ID_Bici integer unique,
                                    Pto_prestamo integer,
                                    Daños integer,
                                    CurrentUse_bic integer
                                );"""

    sql_create_comedores_table = """CREATE TABLE IF NOT EXISTS Comedores (
                                    cedula integer unique,
                                    TypeUser integer,
                                    ComedorSelect integer,
                                    FranjaHoraria integer,
                                    MenuSelect integer,
                                    TurnosDispo integer,
                                    WaitTime integer,
                                    MenuDispo integer,
                                    TurnoActual integer,
                                    Ind_Arrive integer
                                );"""
    
    sql_create_bibliotecas_table = """CREATE TABLE IF NOT EXISTS Bibliotecas (
                                    ID_User integer unique,
                                    ID_Book integer unique,
                                    Number_Book integer,
                                    Number_Biblio integer,
                                    CurrentUse_bib integer
                                );"""


    # create a database connection
    conn = create_connection("bd1.sqlite")

    # create tables
    if conn is not None:
        # create general table
        create_table(conn, sql_create_general_table)

        # create bicicletas table
        create_table(conn, sql_create_bicicletas_table)

        # create comedores table
        create_table(conn, sql_create_comedores_table)

        # create bibliotecas table
        create_table(conn, sql_create_bibliotecas_table)
    else:
        print("Error! cannot create the database connection.")

 
if __name__ == '__main__':
    main()