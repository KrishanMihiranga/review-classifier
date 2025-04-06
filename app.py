from flask import Flask, redirect, render_template, request
from pred_pipeline import preprocessing, vectorizer, get_prediction

app = Flask(__name__)

data = dict()

reviews = []
positive = 0
negative = 0
@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)

@app.route("/", methods=['POST'])
def create():
    review = request.form['review']
    preprocessed_review = preprocessing(review)
    vectorized_preprocessed_review = vectorizer(preprocessed_review)
    prediction = get_prediction(vectorized_preprocessed_review)
    
    if prediction == 'negative':
        global negative
        negative += 1
    else:
        global positive
        positive += 1
    
    reviews.insert(0, review)
    return redirect(request.url)

if __name__ == '__main__':
    app.run()