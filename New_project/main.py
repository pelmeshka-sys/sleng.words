from flask import Flask,render_template 
import random

app = Flask(__name__)

facts_list = [
    "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
    "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
    "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента."
]

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/random_facts")
def func1():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/secret")
def secret():
    return "<h1>Ты нашёл тайную страницу!</h1>"

app.run(debug=True)