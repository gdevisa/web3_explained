from flask import Flask, render_template
app = Flask(__name__)

# routing the decorator function hello_name
@app.route('/')
def hello_name():
    return render_template('index.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')

if __name__ == '__main__':
    app.run(debug = True)
