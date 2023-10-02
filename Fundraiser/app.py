from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', random_number=random.randint(1, 100))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4270)
