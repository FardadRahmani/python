# coding=utf-8
from flask import Flask, render_template, request
from sympy.physics.units import amount

print(__name__)
print(__name__)#__name__=run
app = Flask(__name__)


class Item():
    def __init__(self, name, amount):
        self.name= name
        self.amount= amount



@app.route("/")#rufe fkt auf, wenn browser den schrägstrich aufruft, dann wird rückgabewert an browser geschickt
def hello():
    #items = ["Apfel", "Birne", "Banane"]
    #items = [
     #   Item("Apfel", 5),
    #    Item("Computer", 3),
    #    Item("Birne", 25)
    #]
    items = [
        {"name": "Apfel", "amount": 5},
        {"name": "Computer", "amount": 3},
        {"name": "Birne", "amount": 25}
    ]
    #oder brechnung hier:
    for item in items:
        item["amount"]= item["amount"] * 2

    person= ("Max", "Mustermann")
    # render tut nichts außer die genannte datei zu laden wie man per print sieht
    out= render_template("start.html", nameVar="Max Mustermann", items= items, person=person)
    #name als var muss jetzt auch in der html vorkommen!
    #wichtig: browser kriegt von uns lediglich immer html code ohne jinja2 wie {{nameVar}}, dies aller passiert
    # im HinterGrund auf Server!!! Browser wüsste damit nichts anzufangen!!!!
    print(out)
    return out
    #return "Hello World!"

#Du kannst auch seitens Browser Parameter entgegennehmen per url-Parameter:
# http://127.0.0.1:5000/test3?nameVar=Dado&age=36 -->
@app.route("/test3")
def test3():
    name= request.args.get("nameVar")
    age= request.args.get("age")
    return render_template("test.html", nameVar= name, age= age)

#nicht von python generierte Dateien auszugeben, kümmert sich flask drum (zB style.css) über:
#http://127.0.0.1:5000/static/style.css -->dafür muss es aber in einen ordner static (muss so heißen!)
#oder http://127.0.0.1:5000/static/lib/skeleton/normalize.css
@app.route("/test")
def test():

    paragraph = "<p>HalliHallo Welt!</p>"
    return "Hallo<strong>Test</strong>!" + paragraph

@app.route("/test2")
def test2():
    items= ["Apfel", "Birne", "Banane"]
    output=""

    for item in items:
        output += "<h3>" + item + "</h3>"

    return output# das ist aber mega umständlich! daher templates!siehe test3


@app.route("/currency")
def currency():
    waehr1 = request.args.get("waehrung1", "EUR")
    waehr2 = request.args.get("waehrung2", "DM")
    wkurs= float(request.args.get("wk", "1.95583"))

    wkurs = round(wkurs, 2)
    return render_template("currency.html", waehr1= waehr1, waehr2= waehr2, wkurs= wkurs)