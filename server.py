from flask import Flask
import random

server=Flask(__name__)
choice=random.randint(1,10)

@server.route("/")
def home():
    return '<h1 style= "text-align:center" >Guess a number between 0 and 9</h1>' \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
    
@server.route("/<int:number>")
def guess_number(number):
    if choice<number:
        return '<h1 style= "text-align:center" >Too High, try again!</h1>'\
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="480" height="453" frameBorder="0"/>'
            
    elif choice>number:
        return '<h1 style= "text-align:center" >Too Low, try again!</h1>'\
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="480" height="453" frameBorder="0"/>'
    else:
        return '<h1 style= "text-align:center" >That is correct</h1>'\
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="480" height="453" frameBorder="0"/>'
   
def make_bold(func):
    def wrapper(*args,**kwargs):
        return "<b>"+ func + "<b>"
    return wrapper

if __name__=="__main__":
    server.run(debug=True)   