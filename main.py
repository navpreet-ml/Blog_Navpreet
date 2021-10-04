from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = "janedoe013013@gmail.com"
OWN_PASSWORD = "python013"

all_posts = requests.get("https://api.npoint.io/88c2c1f644ef334058be").json()
print(all_posts)
app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:num>")
def get_post(num):
    return render_template("post.html", num=num, posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Contact Message from Blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)





if __name__ == "__main__":
    app.run(debug=True)
