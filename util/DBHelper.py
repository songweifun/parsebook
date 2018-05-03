import pymysql


class DBHelper:

    conn = ''
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'admin888',
        'database': 'fddx4',
        'charset': 'utf8mb4',
        #'cursorclass': pymysql.cursors.Cursor,
        'cursorclass': pymysql.cursors.DictCursor,
    }

    def __init__(self, db):
        DBHelper.config['database'] = db

    def getConnection(self):
        if DBHelper.conn == '':
            try:
                DBHelper.conn = pymysql.connect(**self.config)
            except Exception:
                print("数据库连接异常")
        print("数据库连接正常")
        return DBHelper.conn


if __name__ == "__main__":
    db1 = DBHelper()
    db2 = DBHelper()
    conn = db1.getConnection()
    conn2 = db2.getConnection()
    print(id(conn))
    print(id(conn2))

    # if conn:
    #     print("数据库连接正常")
    #     conn.close()
    # else:
    #     print("数据库连接异常")
