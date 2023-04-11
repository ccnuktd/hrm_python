import pymysql


from save.SaveInfo import SaveInfo

config = {
    'host': '**.**.**.**',
    'port': 3306,
    'user': 'root',
    'passwd': '******',
    'charset': 'utf8mb4',
}


def create():
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    colum = 'id INT(11) PRIMARY KEY AUTO_INCREMENT, user_name varchar(255), public_time datetime NOT NULL DEFAULT NOW(), level_num ' \
            'SMALLINT, code_length SMALLINT, operation_count SMALLINT '
    create_sql = 'create table if not exists hrm_corporation' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'

    # 创建数据库
    cur.execute('create database if not exists hrm;')
    # 使用数据库
    cur.execute('use hrm;')
    # 设置编码格式
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    # 执行create_sql，创建表
    cur.execute(create_sql)

    conn.close()
    cur.close()


def upload_achieve(info):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute('use hrm;')

    cur.execute("select count(*) from hrm_corporation where user_name=" + "'" + info['user_name'] + "'" + " AND " + "level_num=" + str(info['level_num']))
    if cur.fetchall()[0][0] != 0:
        user_exist = True
    else:
        user_exist = False
    if user_exist:
        query = "update hrm_corporation SET code_length=" + str(info['code_length']) + ", operation_count=" + str(info['operation_count']) + ", public_time=NOW()" + \
            " WHERE user_name=" + "'" + info['user_name'] + "'" + " AND " + "level_num=" + str(info['level_num'])
    else:
        query = "insert into hrm_corporation (user_name, level_num, code_length, operation_count) VALUES ("
        query += "'" + info['user_name'] + "', "
        query += str(info['level_num']) + ", "
        query += str(info['code_length']) + ", "
        query += str(info['operation_count']) + ")"

    try:
        cur.execute(query)
        conn.commit()
    except Exception:
        raise Exception("upload error!")
    finally:
        conn.close()
        cur.close()


def check_user(user_name):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute('use hrm;')

    cur.execute("select count(*) from hrm_corporation where user_name=" + "'" + user_name + "'")
    if cur.fetchall()[0][0] != 0:
        user_exist = True
    else:
        user_exist = False

    conn.close()
    cur.close()

    return user_exist


def fetch(user_name=None, level_num=1, as_code_length=None, as_operation_count=None):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute('use hrm;')

    query = "select user_name, code_length, operation_count from hrm_corporation where level_num=" + str(level_num)
    if user_name:
        query += " AND user_name=" + "'" + user_name + "'"

    if as_code_length is not None:
        if as_operation_count is not None:
            if as_code_length is True and as_operation_count is True:
                query += " ORDER BY code_length asc, operation_count asc"
            elif as_operation_count is True:
                query += " ORDER BY code_length desc, operation_count asc"
            elif as_code_length is True:
                query += " ORDER BY code_length asc, operation_count desc"
            else:
                query += " ORDER BY code_length desc, operation_count desc"
        else:
            if as_code_length is True:
                query += " ORDER BY code_length asc"
            else:
                query += " ORDER BY code_length desc"
    else:
        if as_operation_count is True:
            query += " ORDER BY operation_count asc"
        elif as_operation_count is False:
            query += " ORDER BY operation_count desc"

    cur.execute(query)
    data = cur.fetchall()

    conn.close()
    cur.close()
    return data


if __name__ == "__main__":
    create()
    # data = {
    #     'user_name': 'ktd',
    #     'level_num': 3,
    #     'code_length': 20,
    #     'operation_count': 100
    # }
    # upload_achieve(data)
    # print(fetch())
