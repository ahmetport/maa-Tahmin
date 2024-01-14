from flask import Flask
from markupsafe import escape # güvenli kod yazmak için kullanılıyor


app= Flask(__name__)




@app.route("/") #  http://127.0.0.1:5000
def hello_world():
    return "Hello Televole"

@app.route("/about") #  http://127.0.0.1:5000 /about
def about():
    return "bu sayfa bir data science sayfasidir"

@app.route("/<name>") #  http://127.0.0.1:5000/
def hello_name(name):
    return f"Hello,{escape(name)}!" # guvenlik amaçlı kullanıyoruz 




@app.route("/user/<username>")
def show_user_profil(username):
    return f"User {escape(username)}\'s profile"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"post{post_id}"






if __name__ == "__main__":
    app.run(debug = True)
    
    
    
    