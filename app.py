from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# 支持的平台列表（目前只激活测试平台）
SUPPORTED_PLATFORMS = ["test"]

# HTML 页面模板
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>多平台趋势图抓取工具</title>
</head>
<body>
    <h1>📌 多平台趋势图抓取工具</h1>
    <form method="get" action="/search">
        <label>关键词：</label>
        <input type="text" name="q" required>
        <label>来源平台：</label>
        <select name="platform">
            <option value="test">测试平台</option>
        </select>
        <button type="submit">开始搜索</button>
    </form>
    <hr>
    {% if results %}
        {% for item in results %}
            <img src="{{ item.url }}" alt="test" width="200">
        {% endfor %}
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, results=None)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    platform = request.args.get("platform", "")

    if platform not in SUPPORTED_PLATFORMS:
        return jsonify({"error": "Unsupported platform"})

    # 测试平台返回的图片占位图（使用 via.placeholder.com）
    results = [
        {"source": "test", "url": f"https://via.placeholder.com/300x300.png?text={query}+1"},
        {"source": "test", "url": f"https://via.placeholder.com/300x300.png?text={query}+2"},
        {"source": "test", "url": f"https://via.placeholder.com/300x300.png?text={query}+3"},
    ]

    # 如果是接口访问返回 JSON，否则返回网页
    if request.headers.get("Accept") == "application/json":
        return jsonify({"platform": platform, "query": query, "results": results})
    else:
        return render_template_string(HTML_TEMPLATE, results=results)

if __name__ == "__main__":
    app.run(debug=True)
