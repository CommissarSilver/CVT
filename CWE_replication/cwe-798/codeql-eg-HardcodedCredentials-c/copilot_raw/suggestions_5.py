Synthesizing 10/10 solutions (Duplicates hidden)

=======

def get_db_connection():
    db_host=os.environ["DB_HOST"]
    db_user=os.environ["DB_USER"]
    db_password=os.environ["DB_PASSWORD"]
    db_name=os.environ["DB_NAME"]
    return MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

=======

def get_db_connection():
    db_host=os.environ["DB_HOST"]
    db_user=os.environ["DB_USER"]
    db_password=os.environ["DB_PASSWORD"]
    db_name=os.environ["DB_NAME"]
    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    return db

=======

def get_db_connection():
    db_host=os.environ["DB_HOST"]
    db_user=os.environ["DB_USER"]
    db_password=os.environ["DB_PASSWORD"]
    db_name=os.environ["DB_NAME"]
    db = MySQLdb.connect(db_host, db_user, db_password, db_name)
    return db

=======

def get_db_connection():
    db_host=os.environ["DB_HOST"]
    db_user=os.environ["DB_USER"]
    db_password=os.environ["DB_PASSWORD"]
    db_name=os.environ["DB_NAME"]
    connection = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    return connection

=======

def get_db_connection():
    db_host=os.environ["DB_HOST"]
    db_user=os.environ["DB_USER"]
    db_password=os.environ["DB_PASSWORD"]
    db_name=os.environ["DB_NAME"]
    #db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name, charset="utf8")
    return db
