from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', number1=10, number2=20)
@app.route('/subpage')
def subpage():
    return render_template('body.html', value1=x, value2=y, sum=x+y) 
x=int(input('Enter the first number: '))
y=int(input('Enter the second number: '))


if __name__ == '__main__':

    app.run(debug=True)
    # app.run(host= '0.0.0.0', port=8081)