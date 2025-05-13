from flask import Blueprint, render_template

from pybo.models import Question, Answer

bp = Blueprint('question',__name__,url_prefix='/question')

#질문 목록 페이지
@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',question_list = question_list)

#질문 상세 페이지
@bp.route('/datail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question)