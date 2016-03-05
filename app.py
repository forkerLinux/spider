from flask import Flask, request, render_template
from spider import get_checkcode, simulation_login, simulation_search
"""
http://rd2.zhaopin.com/portal/myrd/regnew.asp?za=2
"""

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        checkcode = request.form['checkcode']
        simulation_login(checkcode)
        # 模拟登录成功
            # if res.status_code == 200:
            # 模拟搜索
            # simulation_search(s)
            # return

@app.route('/img')
def img():
    return get_checkcode()


if __name__ == '__main__':
    app.run(debug=True)
