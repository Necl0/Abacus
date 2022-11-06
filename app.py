from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from werkzeug.datastructures import FileStorage
from pkl_compress import decompress_pickle

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    """Basic route"""
    return render_template('index.html')


def predict_digit(img) -> list[int]:
    """prediction function"""
    # load model

    model = decompress_pickle('model.pbz2')
    
    # predict digit
    prediction = model.predict(img)
    return prediction


@app.route('/', methods=['POST'])
def predict() -> str:
    """Main backend driving function"""
    imagefile: FileStorage = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    img = Image.open(image_path).convert('L')

    # preprocess image
    img = img.resize((28, 28))
    img = np.array(img)
    img = img.reshape(1, 784)

    prediction = predict_digit(img)[0]

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=False)
