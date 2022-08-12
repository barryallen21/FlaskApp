from flask import Flask , render_template , request , redirect , url_for
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('any_html.html')

@app.route('/your-url' , methods= ['GET' , 'POST'] )
def your_url():
    if request.method == 'POST':
        urls = {}
        urls[request.form['short_name']] = {request.form['URL_to_enter']}
        with open('urls.json' , 'w') as url_file:
            json.dump(urls , url_file)
        return render_template('second_html.html' , short_name = request.form['short_name'])
    else:
        return redirect(url_for('hello_world'))

if __name__ == "__main__":
    app.run(debug=True)