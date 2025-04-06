from flask import Flask, render_template,request, redirect
from pred_pipeline import preprocessing, vectorizer, get_prediction
from logger import logging

app = Flask(__name__)

logging.info('Flask server started')

data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative

    logging.info('========== Open home page ============')

    return render_template('index.html', data=data)

@app.route("/", methods = ['post'])
def my_post():
    review = request.form['review']
    logging.info(f'review : {review}')

    preprocessed_review = preprocessing(review)
    logging.info(f'Preprocessed review : {preprocessed_review}')

    vectorized_review = vectorizer(preprocessed_review)
    logging.info(f'Vectorized review : {vectorized_review}')

    prediction = get_prediction(vectorized_review)
    logging.info(f'Prediction : {prediction}')

    if prediction == 'negative':
        global negative
        negative += 1
    else:
        global positive
        positive += 1
    
    reviews.insert(0, review)
    return redirect(request.url)

if __name__ == "__main__":
    app.run()