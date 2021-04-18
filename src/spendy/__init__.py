import os


def get_environ_variable(environ_variable: str, error_message: str) -> str:
    try:
        return os.environ[environ_variable]
    except KeyError:
        raise KeyError(error_message)


SPENDY_HOME = get_environ_variable("SPENDY_HOME", """
'SPENDY_HOME' environment variable does not exist!

Please create a 'SPENDY_HOME' environment variable containing
path to directory where bank CSV data is stored.
""")

DB_CONNECTION_STRING = get_environ_variable(
    "DB_CONNECTION_STRING", """
'DB_CONNECTION_STRING' environment variable does not exist!

Please create a 'DB_CONNECTION_STRING' environment variable containing
a SQLAlchemy connection string for your database. For more info:

https://docs.sqlalchemy.org/en/14/core/engines.html
""")
