from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# 导入指定的配置对象
app.config.from_object('config')
db = SQLAlchemy(app)

# bootstrap = Bootstrap(app)

from app.main import views
from app import models
from app.api import repair
# from app import errors


