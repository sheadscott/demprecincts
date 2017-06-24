import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'MQESU*tm2Wp&Ck*#$8yj&6aY'

RECAPTCHA_PUBLIC_KEY = '6LeSmyAUAAAAAETmNUHlQsKUQev1lyLOpvDBSXEJ'
RECAPTCHA_PRIVATE_KEY = '6LeSmyAUAAAAACoOtSXNXkHLVFZoHQ9u8KtCOygG'

# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'demprecincts@gmail.com'
MAIL_PASSWORD = '69N$B7tyK45VC$Q*jk346%j!'

# administrator list
ADMINS = ['demprecincts@gmail.com']
