from flask import Flask, render_template, request
app = Flask(__name__)#This is App Structure made using Flask


@app.route('/')#Decorator Function
def home():#Function For homepage
    return render_template("index.html") #This will open our main page


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"] #This will accept your name
    Link1 = request.form["link"] #This will accept link
    from pytube import YouTube #Using Pytube For downloading Videos
    YouTube(f'{Link1}').streams.first().download()
    yt = YouTube(f'{Link1}')
    yt.streams
    return f"<h1>Name: {name}, Password: {Link1}</h1> <p> Video Succesfully Downloaded</p>"
#index.html was our html frontend page 
#Now lets start the server

if __name__ == "__main__":
    app.run(debug=True)