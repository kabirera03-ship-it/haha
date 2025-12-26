from flask import Flask

app = Flask(__name__)

@app.route("/")
def print_lyrics():
    lyrics = [
        "Sambhaal ke rakha wo phool mera tu",
        "Meri shayari mein zaroor raha tu",
        "Jo aankhon mein pyaari si duniya basaayi",
        "Wo duniya bhi tha tu, wo lamha bhi tha tu",
        "Haan, lagte hain mujhko ye kisse sataane",
        "Deta na dil mera tujhko bhulaane",
        "Adhoore se vaade, adhoori si raatein",
        "Ab hisse mein daakhil mere bas wo yaadein"
    ]

    output = "<h2>Finding Her:</h2><br>"
    for line in lyrics:
        output += line + "<br>"

    return output

# Required for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
