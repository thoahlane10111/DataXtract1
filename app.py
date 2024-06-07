from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

@app.route('/about')
def about():
    # Render the about.html template
    return render_template('about.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

