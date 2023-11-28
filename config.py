import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="quangnn20-project3.postgres.database.azure.com"
    POSTGRES_USER="quangnn20@quangnn20-project3"
    POSTGRES_PW="Q@2214119qwe" 
    POSTGRES_DB="techconfdb"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://quangproject3.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=zil9PIYoArdKznLhRJrjFSGdcTYHXPRis+ASbF4E10k='
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'boostmytool@gmail.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False