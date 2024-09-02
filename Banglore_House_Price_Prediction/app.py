from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the location names to display in the dropdown list
    locations = model.get_location_names()
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    prediction = model.predict_price(location, total_sqft, bath, bhk)

    return render_template('result.html', price=prediction)

if __name__ == "__main__":
    app.run(debug=True)
