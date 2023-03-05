import os
os.system("pip install openai")
import openai
from flask import Flask, render_template, request, redirect
import json
openai.api_key = "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"

app = Flask(__name__)
global text
text = ""
@app.route('/', methods=["GET", "POST"])
def index():
  if request.method == 'POST':
    text = request.form["user"]
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="write a summary of the following text: " + text,
    temperature=0.8,
    max_tokens=254,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    aw = str(response)
    print(aw)
    aw = aw.replace("\\n", "")
    aw = aw.replace("\\r", "")
    aw = aw[aw.find('"text"') + 9:aw.find('],') - 9]
    aw = aw.replace('"', '')
    return('<!DOCTYPE html><html><head><title>GMI Notes</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="style.css" rel="stylesheet" type="text/css" /><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap" rel="stylesheet">  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"><link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-black.css"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">      <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inconsolata"><style>body, html {height: 100%;font-family: "Inconsolata", sans-serif;}.bgimg {background-position: center;background-color: black;min-height: 69%;}.menu {display: none;}input[type=text], select {width: 100%;padding: 30px 20px;margin: 8px 0;display: inline-block;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;}.bruh{resize: none;}html></style></head><body><div class="w3-white w3-large"><!-- About Container --><div class="w3-container" id="about"><div class="w3-content" style="max-width:700px"><h3>Simplified Notes</h3><p>' +aw+'</p></div></div><!-- Footer --><footer class="w3-center w3-black w3-padding-64 w3-large"><footer class="w3-container w3-padding-32 w3-theme-d1 w3-center"><h4>Follow Us</h4><a class="w3-button w3-large w3-green" href="https://en.wikipedia.org/wiki/Mark_Zuckerberg" title="Facebook"><i class="fa fa-facebook"></i></a><a class="w3-button w3-large w3-green" href="https://en.wikipedia.org/wiki/Elon_Musk" title="Twitter"><i class="fa fa-twitter"></i></a><a class="w3-button w3-large w3-green" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGbWza0UGl3Xph0uy4DFOvBwzUAz6TnY2UmkfIYQFGR95Sf19m4sOu2zRdMRCFE_C7giE:https://i.insider.com/5d8bc40d2e22af423c072962%3Fwidth%3D1136%26format%3Djpeg&usqp=CAU" title="Google +"><i class="fa fa-instagram"></i></a></footer></footer><script>function openMenu(evt, menuName) {var i, x, tablinks;tablinks = document.getElementsByClassName("tablink");for (i = 0; i < x.length; i++) {tablinks[i].className = tablinks[i].className.replace(" w3-dark-grey", "");}document.getElementById(menuName).style.display = "block";evt.currentTarget.firstElementChild.className += " w3-dark-grey";}document.getElementById("myLink").click();</script></html>')
  return render_template("index.html")
app.run()