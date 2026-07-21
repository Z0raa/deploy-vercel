import mysql.connector
from mysql.connector import Error

from config import Config


def get_connection():
    """
    Membuat koneksi ke database MySQL.
    """

    try:
        connection = mysql.connector.connect(
            host="a93mx3.h.filess.io",
            port="3306",
            user="db_akademik_quicksonso",
            password="73233a9cff92bcc133503e840f3fdcf4321a9bbf",
            database="db_akademik_quicksonso"
        )

        return connection

    except Error as e:
        print(f"Gagal terhubung ke database: {e}")
        return None