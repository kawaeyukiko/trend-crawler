from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    platform = request.args.get("platform")

    if not query or not platform:
        return jsonify({"error": "Missing query or platform"}), 400

    results = []
    if platform == "pinterest":
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        url = f"https://www.pinterest.com/search/pins/?q={query}"
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                # 简单模拟数据：真实项目应用抓取库解析 HTML 或通过API获取
                results = [
                    {"source": "pinterest", "url": f"https://source.unsplash.com/400x300/?{query}+1"},
                    {"source": "pinterest", "url": f"https://source.unsplash.com/400x300/?{query}+2"},
                    {"source": "pinterest", "url": f"https://source.unsplash.com/400x300/?{query}+3"},
                ]
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif platform == "google":
        results = [
            {"source": "google", "url": f"https://source.unsplash.com/400x300/?{query}+google1"},
            {"source": "google", "url": f"https://source.unsplash.com/400x300/?{query}+google2"},
        ]

    elif platform == "bing":
        results = [
            {"source": "bing", "url": f"https://source.unsplash.com/400x300/?{query}+bing1"},
            {"source": "bing", "url": f"https://source.unsplash.com/400x300/?{query}+bing2"},
        ]

    else:
        return jsonify({"error": "Unsupported platform"}), 400

    return jsonify(results)
