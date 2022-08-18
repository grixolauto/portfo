import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<path:page_name>')
def navigation(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data_in_dict = request.form.to_dict()
            write_to_csv(data_in_dict)
            return redirect('/thankyou.html')
        except:
            return 'Something wrong with database'
    else:
        return 'Something wrong, try again!'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        database.write(data['email'] + '\n')
        database.write(data['subject'] + '\n')
        database.write(data['message'] + '\n\n')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([data['email'], data['subject'], data['message']])


if __name__ == '__main__':
    app.run(debug=True)
