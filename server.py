from flask import Flask, render_template, request,redirect
import csv

app = Flask(__name__)



# - to return the index.html
# - since it is in the same folder
#   dont have to include the actual path
# ./ means current directory
# need to create a folder templates if we
# are gg to add them in using render Template

@app.route("/")
#like initialising in the parameter
def my_home():
    return render_template('index.html')

# @app.route("/<username>/<int:post_id>")
# #like initialising in the parameter
# def hello_world(username=None, post_id = None):
#     return render_template('index.html', name= username, post_id = post_id)

# if 2 routes are the same then its gonna 
# follow the function in the first route

#@app.route("/favicon.ico")
# def blog():
#     return "<p>Welcome to my blog!</p>"

# To generate dynamic routes for the other html pages

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "<p>This is my dog!</p>"

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline= '') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # this way we always add a new line when we append
        csv_writer = csv.writer(database2, delimiter = ',', quotechar ='"', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])




# Get means the browser wants us to send the information
# Post means the browsers wants us to save the information

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            #turning the form data into a dict
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return 'did not save to database'
    else:
        return "something went wrong. Try again"

