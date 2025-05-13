from pybo import db

class Question(db.Model):
    #질문 데이터의 고유 번호
    id = db.Column(db.Integer, primary_key=True)
    #질문 제목
    subject = db.Column(db.String(200), nullable=False)
    #질문 내용
    content = db.Column(db.Text(), nullable=False)
    #질문 작성일시
    create_date = db.Column(db.DateTime(), nullable=False)    

class Answer(db.Model):
    #답변 데이터의 고유 번호
    id = db.Column(db.Integer, primary_key=True)
    #질문 데이터의 고유 번호
    question_id = db.Column(db.Integer,db.ForeignKey('question.id',ondelete='CASCADE'))
    question=db.relationship('Question',backref=db.backref('answer_set',cascade='all, delete-orphan'))
    #답변 내용
    content = db.Column(db.Text(), nullable=False)
    #답변 작성일시
    create_date = db.Column(db.DateTime(), nullable=False)    