from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

IMGBB_API_KEY = os.environ.get("IMGBB_API_KEY")  # 从环境变量读取你的 imgbb Key

# ----------- 平台抓图逻辑 -----------
def search_pinterest_images(query):
    return [
        f"https://i.pinimg.com/564x/fake1.jpg",
        f"https://i.pinimg.com/564x/fake2.jpg",
        f"https://i.pinimg.com/564x/fake3.jpg"
    ]

def search_bing_images(query):
    return [
        f"https://www.bing.com/fake1.jpg",
        f"https://www.bing.com/fake2.jpg",
        f"https://www.bing.com/fake3.jpg"
    ]

def search_google_images(query):
    return [
        f"https://www.google.com/fake1.jpg",
        f"https://www.google.com/fake2.jpg",
        f"https://www.google.com/fake3.jpg"
    ]

# ----------- 图床上传 -----------
def upload_to_imgbb(image_url):
    if not IMGBB_API_KEY:
        return image_url
    try:
        res = requests.post("https://api.imgbb.com/1/upload", params={
            "key": IMGBB_API_KEY,
            "image": image_url
        })
        data = res.json()
        return data["data"]["url"]
    except:
        return image_url

# ----------- 网页界面 -----------
@app.route("/")
def index():
    return render_template("index.html")

# ----------- 搜图 API -----------
@app.route("/search")
def search():
    query = request.args.get("q")
    platform = request.args.get("platform")

    if not query or not platform:
        return jsonify({"error": "Missing query or platform"})

    if platform == "pinterest":
        urls = search_pinterest_images(query)
    elif platform == "bing":
        urls = search_bing_images(query)
    elif platform == "google":
        urls = search_google_images(query)
    else:
        return jsonify({"error": "Unsupported platform"})

    final_results = [{"url": upload_to_imgbb(url), "source": platform} for url in urls]
    return jsonify(final_results)

if __name__ == "__main__":
    app.run(debug=True)
