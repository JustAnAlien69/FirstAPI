from flask import Flask, jsonify, request
 
app = Flask(__name__)

MyData = [
    {
        "Name":"Aanya",
        "Grade":"9",
        "School":"Ecole McTavish"
    },
    {
        "Fav-Game":"Minecraft",
        "Hobby":"Reading",
    }
]

@app.route("/")
def myFirstAPI():
    return "This is my first API and this is the data I'm adding."


@app.route("/MyData")
def MyDataAPI():
    return jsonify({
        "Data" : MyData
    })

@app.route("/AddData", methods=["POST"])
def addingData():
    newData = {
        "My Favorite Movie":"The Maze Runner",
        "Favourite Book Series":"Calvin & Hobbes",
        "Favourite Song":"Underground by MISSIO"
    }
    MyData.append(newData)
    return jsonify({
        "message":"newData is added",
        "Data" : MyData
    })

if __name__ == "__main__":
    app.run()
