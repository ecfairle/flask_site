from app import db
from datetime import datetime
import bcrypt


class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self._set_password(password)
        self.email = email
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)

    def _set_password(self,unhashed):
        self.password = bcrypt.hashpw(unhashed.encode('UTF-8'), bcrypt.gensalt())

    def validate_password(self,pw):
        return bcrypt.checkpw(pw.encode('UTF-8'), self.password.encode('UTF-8'))

    def __repr__(self):
        return '<User %r>' % (self.username)
