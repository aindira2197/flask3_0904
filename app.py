from flask import Flask, render_template

app = Flask(__name__)

sonlar = [14, 8, 33, 5, 71, 22, 9, 46]

@app.route('/sonlar/juft')
def juft_sonlar():
    juft = [son for son in sonlar if son % 2 == 0]

    return render_template(
        'juft.html',
        juft_sonlar=juft
    )

if __name__ == "__main__":
    app.run(debug=True)
