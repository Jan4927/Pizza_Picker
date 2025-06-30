from flask import Flask, request, jsonify

app = Flask(__name__)

PIZZAS = [
    {"name": "Margherita", "vegetarian": True, "spicy": False},
    {"name": "Pepperoni",  "vegetarian": False, "spicy": False},
    {"name": "Diavola",    "vegetarian": False, "spicy": True},
    {"name": "Funghi",     "vegetarian": True,  "spicy": False},
]

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/pick")
def pick():
    data = request.get_json(force=True) or {}
    vegetarian = data.get("vegetarian")
    spicy      = data.get("spicy")
    for p in PIZZAS:
        if (vegetarian is None or p["vegetarian"] == vegetarian)                    and (spicy is None or p["spicy"] == spicy):
            return jsonify(p)
    return {"error": "no matching pizza"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
