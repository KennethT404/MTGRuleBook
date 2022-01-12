from flask import Flask, render_template,redirect, request, url_for

app = application = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/turn')
def turn():
    return render_template('mtg-turn-home.html')

@app.route('/oopsie')
def filler():
    return render_template('fillerpage.html')

@app.route('/turn/Beginning_Phase')
def beginphase():
    return render_template('beginning-phase.html')

@app.route('/turn/Main_Phase')
def mainphase():
    return render_template('main-phase.html')

# @app.route('/turn/Combat_Phase')
# def beginphase():
#     return render_template('combat-phase.html')

# @app.route('/turn/Ending_Phase')
# def beginphase():
#     return render_template('end-phase.html')

# @app.route('/test', methods= ['POST','GET'])
# def test():
#     if request.method =='POST':
#         name = request.form['cname']
#         return redirect(url_for('', name = name))
#     else:
#         return render_template('card-search.html')
print(${{env.text_env}})
if __name__ =='__main__':
    app.run(debug=True)
