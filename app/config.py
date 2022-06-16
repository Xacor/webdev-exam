import os

SECRET_KEY = 'bc19682532d598bee940dfd34c91380ddde73580d16de643cce645b8cb100384'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_1611_exam:stepbrohelpme@std-mysql.ist.mospolytech.ru/std_1611_exam'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

ADMIN_ROLE_ID = 2
MODER_ROLE_ID = 3

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')