from config.default import *
from logging.config import dictConfig

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='vERYlONGpASSWORD!!!',
    url='ls-89ba7ee2fba281bddc1a25ebc3a1ad4a3332159f.cordcckkaqsz.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xd5\xb4\x95\xd2\x12\xbb\x94\xa23yw\xf7\x8e7\xd5q'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5, # 5MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
