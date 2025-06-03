import tensorflow
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model1 = load_model('CNN-Flowers-Model1.h5')
model2 = load_model('CNN-Flowers-Model2.h5')
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

def predict_image(model, filepath):
    img = load_img(filepath, target_size=(128, 128))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0 
    predictions = model.predict(img_array, verbose=0)[0]
    predicted_class = class_names[np.argmax(predictions)]
    percentages = [(class_names[i], round(predictions[i] * 100, 2)) for i in range(len(class_names))]
    percentages.sort(key=lambda x: x[1], reverse=True)
    return predicted_class, percentages

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction1 = None
    prediction2 = None
    filename = None
    percentages1 = []
    percentages2 = []

    if request.method == 'POST':
        if 'file' in request.files and request.files['file'].filename != '':
            file = request.files['file']
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            prediction1, percentages1 = predict_image(model1, filepath)
            prediction2, percentages2 = predict_image(model2, filepath)

    return render_template(
        'index.html',
        prediction1=prediction1,
        prediction2=prediction2,
        percentages1=percentages1,
        percentages2=percentages2,
        filename=filename
    )

if __name__ == '__main__':
    app.run(debug=True)