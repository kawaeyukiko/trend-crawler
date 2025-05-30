from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

def fetch_pinterest_images(query):
    # 示例：真实抓图逻辑可接入 Pinterest API 或第三方抓图工具
    return [
        {"source": "pinterest", "url": f"https://i.pinimg.com/236x/dummy1.jpg"},
        {"source": "pinterest", "url": f"https://i.pinimg.com/236x/dummy2.jpg"},
    ]

def fetch_google_images(query):
    return [
        {"source": "google", "url": f"https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"},
        {"source": "google", "url": f"https://www.google.com/images/branding/product/ico/googleg_lodp.ico"},
    ]

def fetch_bing_images(query):
    return [
        {"source": "bing", "url": f"https://www.bing.com/th?id=OHR.dummy1"},
        {"source": "bing", "url": f"https://www.bing.com/th?id=OHR.dummy2"},
    ]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    platform = request.args.get("platform")

    if not query or not platform:
        return jsonify({"error": "Missing query or platform"}), 400

    if platform == "pinterest":
        data = fetch_pinterest_images(query)
    elif platform == "google":
        data = fetch_google_images(query)
    elif platform == "bing":
        data = fetch_bing_images(query)
    else:
        return jsonify({"error": "Unsupported platform"}), 400

    return jsonify({
        "platform": platform,
        "query": query,
        "results": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
