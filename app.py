from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


def predict_digit(img):
    # load model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    # predict digit
    prediction = model.predict(img)
    return prediction

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    prediction = predict_digit(imagefile)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
