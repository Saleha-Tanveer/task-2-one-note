from datetime import datetime
from database import db
# from run import ma

class Note(db.Model):
    __tablename__='Note hi note zindagi mein ... aahahhaha'
    id =db.Column('note_id',db.Integer,primary_key=True)
    category=db.Column('category',db.String(50),nullable=False)
    note_title=db.Column('note_title',db.String(50),nullable=False)
    description=db.Column('description',db.Text(),nullable=False)s
    date_created=db.Column('date_created',db.DateTime,default=datetime.now)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))


    def __init__(self,note_title,category,description,user_id):
        self.note_title=note_title
        self.category=category
        self.description=description
        self.user_id=user_id

    def serialize(self):
        return {'note_id': self.id, 'category': self.category, 'note_title': self.note_title,
                'description': self.description, 'date_created': self.date_created}