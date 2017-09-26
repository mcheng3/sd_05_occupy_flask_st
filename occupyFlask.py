import occupation
from flask import Flask, render_template

print(occupation.pickOccupation())

my_app = Flask(__name__)

@my_app.route('/occupations')
def displayOccupation():
    
    return render_template('one.html', job = occupation.pickOccupation())

if __name__ == '__main__':
        my_app.debug = True
        my_app.run()
