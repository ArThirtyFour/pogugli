from flask import Flask, request , render_template , redirect
from bd import add_url, get_url_for_id 
app = Flask(__name__ , static_folder='templates')

    

@app.route('/')
def main():
    return render_template('send/index.html')


@app.route('/search/<id>')
def get_url(id):
    res = get_url_for_id(id)
    if res == 'Нет такой ссылки':
        return redirect('/')
    else:
        res_result = 'https://www.google.com/search?q=' + res.replace(' ', '+')
        return render_template('result/index.html', res=res, url=res_result)



@app.route('/api/get_url', methods=['POST'])
def add_url_1():
    data = request.form['zapros']
    if data == '':
        return 'Нет данных'
    else:
        res = add_url(data)
        return '{}'.format(res)



if __name__ == '__main__':
    app.run(port=5500,debug=True)