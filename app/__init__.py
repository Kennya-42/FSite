from flask import Flask, render_template
from flask_zurb_foundation import Foundation


app = Flask(__name__)
    
Foundation(app)
    
@app.route('/')
def index():
     return render_template('index.html')


@app.route('/resume/')
def resume():
     return render_template('viewer.html')
    
@app.route('/about/')
def about():
     return render_template('about.html',title='about')



if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)


