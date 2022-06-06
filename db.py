import sqlite3 as lite

conn = lite.connect('db_trabalho.db')

def criarDB():
   with conn:
       cursor = conn.cursor()
       cursor.execute(
           '''CREATE TABLE hqs_tb(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           titulo TEXT,
           publicadora TEXT,
           editora TEXT,
           status BOOLEAN,
          comentario TEXT,
           )'''
       )

def inserir(data):
    with conn:
        cursor = conn.cursor()
        query = '''
        INSERT INTO 
            hqs_tb
            (titulo, publicadora, editora, status, comentario)
        VALUES
            (?,?,?,?,?)
        '''
        cursor.execute(query, data)

def listar():
    dados= []
    with conn:
        cursor = conn.cursor()
        query = "SELECT * FROM hqs_tb"
        cursor.execute(query)
        data = cursor.fetchall()

        for i in data:
            dados.append(i)
    return dados

def atualizar(data):
    with conn:
        cursor = conn.cursor()
        query = '''
        UPDATE hqs_tb 
            SET
            (
                titulo = ?, 
                publicadora = ?, 
                editora = ?, 
                status = ?, 
                comentário = ?
            )
        WHERE id = ?
        '''
        cursor.execute(query, data)

def deletar(id):
    with conn:
        cursor = conn.cursor()
        query = "DELETE FROM hqs_tb WHERE id = ?"
        cursor.execute(query, id)