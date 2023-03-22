from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    # code to fetch portfolio data from database or file
    portfolio_data = [ 
        {"name": "Design 1", "image_url": "https://example.com/design1.jpg", "price": 50},
        {"name": "Design 2", "image_url": "https://example.com/design2.jpg", "price": 75},
        {"name": "Design 3", "image_url": "https://example.com/design3.jpg", "price": 100},
    ]
    return render_template('portfolio.html', portfolio_data=portfolio_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # code to process the contact form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # code to send an email to the website owner with the contact information
        return render_template('thankyou.html')
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
