
class MyCrud:
    def __init__(self):
        import sqlite3
        self.conexao = sqlite3.connect('db.sqlite3')
        self.cursor = self.conexao.cursor()

        sql = '''
            CREATE TABLE IF NOT EXISTS pessoas(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                cpf VARCHAR(11) NOT NULL,
                nome TEXT(30) NOT NULL
            );
        '''
        self.cursor.execute(sql)
        print('ok')

    def fechardb(self):
        self.conexao.close()

    def ler(self):
        sql = """
            SELECT * FROM pessoas;
        """
        for i in self.cursor.execute(sql).fetchall():
            print(i)

    def inserir(self, cpf, nome):
        sql = """
            INSERT INTO pessoas(cpf,nome)
            values(?,?);
        """
        self.cursor.execute(sql, (cpf, nome))
        self.conexao.commit()

    def alterar(self, id, cpf, nome):
        sql = """
            UPDATE pessoas
            SET cpf = ?, nome = ?;
            WHERE id = ?;
        """
        self.cursor.execute(sql, (cpf, nome, id))
        self.conexao.commit()

    def deletar(self, id):
        sql = """
            DELETE FROM pessoas
            WHERE id = ?;
        """
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
