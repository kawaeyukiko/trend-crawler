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

    # 示例返回固定占位图（后续接入爬虫或 API 替换）
    dummy_image_urls = [
        f"https://via.placeholder.com/300?text={query}+1",
        f"https://via.placeholder.com/300?text={query}+2",
        f"https://via.placeholder.com/300?text={query}+3"
    ]

    uploaded_urls = []
    for url in dummy_image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            r = requests.post(
                "https://api.imgbb.com/1/upload",
                params={"key": IMGBB_API_KEY},
                files={"image": response.content}
            )
            if r.status_code == 200:
                data = r.json()
                uploaded_urls.append(data["data"]["url"])
    
    return jsonify({"results": uploaded_urls})

@app.route("/")
def index():
    return "服务已部署成功！请使用 /search?q=关键词&platform=xxx 进行调用"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
