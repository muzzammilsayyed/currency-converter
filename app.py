from flask import Flask, render_template, request
from currency_converter import CurrencyConverter

app = Flask(__name__ )
converter = CurrencyConverter()

@app.route('/')
def index():
    # Get list of available currencies from the currency_converter library
    currencies = converter.currencies

    # Render the index.html template with the list of currencies
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    
    # Perform currency conversion
    result = converter.convert(amount, from_currency, to_currency)
    
    # Render the result.html template with the conversion result
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
