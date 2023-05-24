from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    account_server = os.getenv("ACCOUNT_SERVICE")
    account_server_port = os.getenv("ACCOUNT_SERVICE_PORT")
    book_server = os.getenv("BOOK_SERVICE")
    book_server_port = os.getenv("BOOK_SERVICE_PORT")
    database = os.getenv("SQLALCHEMY_DATABASE_URI")
