from flask import Flask, render_template, request
import pickle
from PIL import Image
import numpy as np

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
    # load imagefile content from image_path
    img = Image.open(image_path)

    # preprocess image
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1, 784)


    prediction = predict_digit(img)


    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
