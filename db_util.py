import pymysql


class Db_Util:
    def __init__(self, db_name):
        print("Initializing connection with %s" % (db_name))
        self.database = pymysql.connect('localhost', 'root', '', db_name)
        self.cursor = self.database.cursor()

    def __del__(self):
        print("Closing connection...")
        self.cursor.close()
        self.database.close()

    def get_all(self, table_name):
        sql = "SELECT * FROM %s ORDER BY id desc" % (table_name)
        self.cursor.execute(sql)
        rows = []
        for row in self.cursor:
            entry = {'id': row[0], 'name': row[1], 'designation': row[2], 'phone': row[3]}
            rows.append(entry)
        return rows

    def add_record(self, table_name, json_data):

        sql = "INSERT INTO %s VALUES(NULL, '%s', '%s', '%s')"\
              % (table_name, json_data.get('name'), json_data.get('designation'), json_data.get('phone'))
        self.cursor.execute(sql)
        self.database.commit()

    def delete_record(self, table_name, id):

        sql = "DELETE FROM %s WHERE id = '%s'"\
              % (table_name,id)
        self.cursor.execute(sql)
        self.database.commit()

    def search_record(self, table_name, json_data):

        name = json_data.get('name')
        designation = json_data.get('designation')
        phone = json_data.get('phone')

        sql = "SELECT * FROM %s " %(table_name)
        where_clause = ""
        if len(name)>0:
            where_clause += "name LIKE '%"+name+"%' "

        if len(designation)>0:
            if len(where_clause) != 0:
                where_clause += "AND "
            where_clause += "designation LIKE '%"+designation+"%' "

        if len(phone)>0:
            if len(where_clause) != 0:
                where_clause += "AND "
            where_clause += "phone LIKE '%"+phone+"%' "

        if len(where_clause) != 0:
            sql += "WHERE "+where_clause

        print (sql)
        self.cursor.execute(sql)
        rows = []
        for row in self.cursor:
            entry = {'id': row[0], 'name': row[1], 'designation': row[2], 'phone': row[3]}
            rows.append(entry)
        return rows
