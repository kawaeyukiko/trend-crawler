from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

def upload_to_imgbb(image_url):
    try:
        response = requests.post(
            "https://api.imgbb.com/1/upload",
            params={"key": IMGBB_API_KEY},
            data={"image": image_url},
        )
        result = response.json()
        return result["data"]["url"] if result.get("data") else image_url
    except:
        return image_url

def search_bing_images(query):
    # 示例替代方案：返回虚拟图片
    return [
        f"https://via.placeholder.com/300x300?text={query}+A",
        f"https://via.placeholder.com/300x300?text={query}+B"
    ]

def search_pinterest_images(query):
    return [
        f"https://via.placeholder.com/300x300?text={query}+Pin1",
        f"https://via.placeholder.com/300x300?text={query}+Pin2"
    ]

@app.route("/search")
def search():
    query = request.args.get("q", "")
    platform = request.args.get("platform", "bing")

    if not query:
        return jsonify({"error": "Missing query"}), 400

    # 路由分发
    if platform == "bing":
        raw_images = search_bing_images(query)
    elif platform == "pinterest":
        raw_images = search_pinterest_images(query)
    else:
        return jsonify({"error": "Unsupported platform"}), 400

    results = [{"source": platform, "url": upload_to_imgbb(url)} for url in raw_images]
    return jsonify({"platform": platform, "query": query, "results": results})
