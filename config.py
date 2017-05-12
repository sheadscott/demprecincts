import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'MQESU*tm2Wp&Ck*#$8yj&6aY'

RECAPTCHA_PUBLIC_KEY = '6LeSmyAUAAAAAETmNUHlQsKUQev1lyLOpvDBSXEJ'
RECAPTCHA_PRIVATE_KEY = '6LeSmyAUAAAAACoOtSXNXkHLVFZoHQ9u8KtCOygG'

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['sheadscott@gmail.com']
