from flask import Flask

app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def words(word):
    #word를 찾아서 뜻을 보여준다.
    my_dict = {'apple':'사과', 'banana':'바나나', 'melon':'멜론'}
    if word in my_dict.keys():
        return f'{word}은(는) {my_dict[word]}!'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'