import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c301dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sriblog123@gmail.com'
    MAIL_PASSWORD = 'Zxcvbnm@1'
