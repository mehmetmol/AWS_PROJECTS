from flask import Flask 
app = Flask(__name__)
@app.route('/')
def head():
    return 'Hello World ?!'
@app.route('/secondpage')
def second():
    return 'This is the second page'
@app.route('/third')
def third():
    return 'This is the third page'
@app.route('/fourth/<string:id>')
def fourth(id):
    return f'id of this page is {id}' 


if __name__ == '__main__':

    #app.run(debug=True)
    app.run(host= '0.0.0.0', port=80)