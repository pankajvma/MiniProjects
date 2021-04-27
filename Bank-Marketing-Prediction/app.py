import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

def get_full_data(form_input):
    # form_input = [23, 1, 15, 125, 5, 1, 0, 0, 0]

    add_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    add_data[form_input[8]] = 1
    add_data[form_input[9] + 11] = 1

    model_input = form_input[: 8]
    model_input.extend(add_data)

    return model_input

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]

    print(int_features) 

    all_int_features = get_full_data(int_features)

    print(all_int_features) 

    final_features = [np.array(all_int_features)]
    prediction = model.predict(final_features)

    output = 'is more likely to' if prediction == 1 else 'might not'

    return render_template('index.html', prediction_text= f'This customer {output} Subscribe to the Term Deposit.')


if __name__ == "__main__":
    app.run(debug=True)