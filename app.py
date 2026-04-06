from flask import Flask, render_template, request
import os

app = Flask(__name__)

# MENU DATA
menu = {
    "Butter Masala Dosa": 70,
    "Masala Dosa": 60,
    "Butter Dosa": 60,
    "Set Butter Dosa": 60,
    "Set Dosa": 50,
    "Plain Dosa": 40,
    "Kali Dosa": 30,
    "Tatte Idli": 50,
    "Tatte Idli + Vada": 75,
    "Vada": 25,
    "Coffee": 20
}

orders = []
total_sales = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global total_sales

    message = ""

    if request.method == "POST":
        item = request.form.get("item")
        table = request.form.get("table")

        if item in menu:
            price = menu[item]
            total_sales += price

            orders.append({
                "item": item,
                "table": table,
                "price": price
            })

            message = f"Order Confirmed: {item} for Table {table}"

    return render_template("index.html", menu=menu, message=message or "", sales=total_sales or 0, orders=orders or [])

# SIMPLE AI CHATBOT
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form.get("message").lower()

    if "menu" in user_msg:
        reply = "We have dosa, idli, vada, coffee"
    elif "suggest" in user_msg:
        reply = "Try Butter Masala Dosa 😋"
    elif "table" in user_msg:
        reply = "We have 10 tables available"
    else:
        reply = "Sorry, I didn't understand"

    return reply


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
