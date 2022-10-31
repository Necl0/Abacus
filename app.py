from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def predict_digit(img):
    # load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    # predict digit
    prediction = model.predict(img)
    return prediction


@app.route('/upload', methods=['POST'])
def result():
    if request.method == 'POST':
        img = request.files['img']
        prediction = predict_digit(img)
        return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
