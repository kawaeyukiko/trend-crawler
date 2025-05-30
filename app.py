from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>多平台趋势图抓取工具</title>
        <style>
            body { font-family: sans-serif; padding: 20px; }
            img { width: 150px; height: 150px; margin: 10px; }
        </style>
    </head>
    <body>
        <h1>📌 多平台趋势图抓取工具</h1>
        <form onsubmit="search(); return false;">
            <label>关键词：</label>
            <input type="text" id="query" required>
            <label>来源平台：</label>
            <select id="platform">
                <option value="test">测试平台</option>
            </select>
            <button type="submit">开始搜索</button>
        </form>
        <div id="results"></div>
        <script>
            function search() {
                const query = document.getElementById("query").value;
                const platform = document.getElementById("platform").value;
                fetch(`/search?q=${encodeURIComponent(query)}&platform=${platform}`)
                    .then(res => res.json())
                    .then(data => {
                        const resultsDiv = document.getElementById("results");
                        resultsDiv.innerHTML = "";
                        if (data.results) {
                            data.results.forEach(item => {
                                const img = document.createElement("img");
                                img.src = item.url;
                                img.alt = item.source;
                                resultsDiv.appendChild(img);
                            });
                        } else {
                            resultsDiv.innerText = "未返回图片";
                        }
                    });
            }
        </script>
    </body>
    </html>
    """)

@app.route("/search")
def search():
    query = request.args.get("q")
    platform = request.args.get("platform")
    if platform != "test":
        return jsonify({"error": "Unsupported platform"})

    # 使用 dummyimage.com 作为占位图
    results = [
        {"source": "test", "url": f"https://dummyimage.com/300x300/ccc/000&text={query}+1"},
        {"source": "test", "url": f"https://dummyimage.com/300x300/999/fff&text={query}+2"},
        {"source": "test", "url": f"https://dummyimage.com/300x300/666/fff&text={query}+3"},
    ]
    return jsonify({"platform": platform, "query": query, "results": results})

if __name__ == "__main__":
    app.run(debug=True)
