from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# 模拟支持的平台
SUPPORTED_PLATFORMS = ['test', 'pinterest', 'bing']

IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("q")
    platform = request.args.get("platform")

    if platform not in SUPPORTED_PLATFORMS:
        return jsonify({"error": "Unsupported platform"})

    # 示例数据（测试平台用）
    results = []
    if platform == 'test':
        results = [
            {"source": "test", "url": f"https://imgplaceholder.com/300x300/cccccc/000000?text={query}+1"},
            {"source": "test", "url": f"https://imgplaceholder.com/300x300/999999/000000?text={query}+2"},
            {"source": "test", "url": f"https://imgplaceholder.com/300x300/666666/ffffff?text={query}+3"},
        ]

    return jsonify({
        "platform": platform,
        "query": query,
        "results": results
    })

if __name__ == '__main__':
    app.run()
