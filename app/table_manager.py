import sqlite3

CREATE_USERS_TABLE_QUERY = 'create table if not exists USERS(USERID INTEGER PRIMARY KEY AUTOINCREMENT,EMAIL TEXT NOT NULL UNIQUE,PASSWORD TEXT NOT NULL,USERNAME TEXT);'
CREATE_SUBSCRIPTIONS_TABLE_QUERY = 'create table if not exists SUBSCRIPTIONS(SUBID INTEGER PRIMARY KEY AUTOINCREMENT,PRODUCTURL TEXT NOT NULL,USER INTEGER,FOREIGN KEY(USER) REFERENCES USERS(USERID));'
ADD_NEW_USER_QUERY = 'insert into USERS(EMAIL,PASSWORD,USERNAME) values (?,?,?)'
GET_PASSWORD_QUERY = 'select PASSWORD from USERS where EMAIL=?'


def create_connection():
    conn = sqlite3.connect('Amazon_Price_Tracker.db')
    return conn


def create_tables():
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute(CREATE_USERS_TABLE_QUERY)
        c.execute(CREATE_SUBSCRIPTIONS_TABLE_QUERY)
        conn.commit()
        return 1
    except Exception as e:
        print(e)
        return -1
    finally:
        conn.close()


def add_user(p_email, p_pass):
    conn = create_connection()
    c = conn.cursor()
    try:
        uname = p_email.strip().lower()[:p_email.find('@')]
        # QUERY = ADD_NEW_USER_QUERY.replace("VAL_EMAIL", p_email.strip().lower()).replace(
        #     "VAL_PASS", p_pass).replace("VAL_UNAME", uname)
        c.execute(ADD_NEW_USER_QUERY, (p_email.strip().lower(), p_pass, uname))
        conn.commit()
        return 1
    except Exception as e:
        print(e)
        return -1
    finally:
        conn.close()


def check_user(p_email, p_pass):
    create_tables()
    conn = create_connection()
    c = conn.cursor()
    try:
        p_email = p_email.strip().lower()
        c.execute(GET_PASSWORD_QUERY, (p_email,))
        var_pass = None
        for v in c:
            if v:
                var_pass = v[0]
        if var_pass and var_pass == p_pass:
            return 10
        elif var_pass and var_pass != p_pass:
            return 11
        else:
            r = add_user(p_email, p_pass)
            if r == 1:
                conn.commit()
                return 12
            else:
                return -1

    except Exception as e:
        print(e)
        return -1
    finally:
        conn.close()


# print add_user("Test3@asds","Pass3")
# check_user("Test1@asds", "Pass1")

# print create_tables()
# conn = create_connection()
# c = conn.cursor()
# c.execute("drop table USERS")
# for v in c:
# 	print v[0],v[1]

if __name__ == "__main__":
    print "Entered main"
    conn = create_connection()
    c = conn.cursor()
    add_user("testemail@mac.com", "testpassword1")
    c.execute("select * from USERS")
    for v in c:
        print v
