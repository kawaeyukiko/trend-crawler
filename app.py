from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 Trend Crawler 已部署成功！请访问 /search 试试"

@app.route("/search")
def search():
    query = request.args.get("q", "测试关键词")
    platform = request.args.get("platform", "google")
    
    # 返回模拟的3张图片
    images = [
        {"url": f"https://imgplaceholder.com/300x300/cccccc/000000?text={query}+1", "source": platform},
        {"url": f"https://imgplaceholder.com/300x300/999999/000000?text={query}+2", "source": platform},
        {"url": f"https://imgplaceholder.com/300x300/666666/ffffff?text={query}+3", "source": platform}
    ]
    
    return jsonify({
        "query": query,
        "platform": platform,
        "results": images
    })

if __name__ == "__main__":
    app.run()
