#작성시간 템플릿 필터
def format_datetime(value,fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime(fmt)