from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

@app.route("/search")
def search():
    query = request.args.get("q")
    platform = request.args.get("platform", "google")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    dummy_urls = [
        "https://via.placeholder.com/300x200.png?text=Sample+1",
        "https://via.placeholder.com/300x200.png?text=Sample+2"
    ]

    uploaded_urls = []
    for url in dummy_urls:
        res = requests.post(
            "https://api.imgbb.com/1/upload",
            params={"key": IMGBB_API_KEY},
            data={"image": url}
        )
        try:
            uploaded_urls.append(res.json()["data"]["url"])
        except:
            continue

    return jsonify({"results": uploaded_urls})

if __name__ == "__main__":
    app.run()
