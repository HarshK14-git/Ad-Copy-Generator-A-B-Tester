from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from ad_generator import (
    generate_ad_copies,
    results_to_csv,
    results_to_notion
)
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/generate", methods=["POST", "OPTIONS"])
def generate():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    try:
        data        = request.json
        product     = data.get("product", "").strip()
        description = data.get("description", "").strip()
        audience    = data.get("audience", "").strip()
        platforms   = data.get("platforms", ["google"])
        tone        = data.get("tone", "professional")
        variations  = int(data.get("variations", 3))

        if not product:
            return jsonify({"error": "Product name is required"}), 400
        if not platforms:
            return jsonify({"error": "Select at least one platform"}), 400

        results = generate_ad_copies(
            product, description, audience,
            platforms, tone, variations
        )

        return jsonify({
            "success": True,
            "product": product,
            "audience": audience,
            "tone": tone,
            "results": results
        })

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"error": str(e)}), 500


@app.route("/export/csv", methods=["POST", "OPTIONS"])
def export_csv():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    try:
        data    = request.json
        product = data.get("product", "campaign")
        results = data.get("results", {})
        csv     = results_to_csv(product, results)
        return Response(
            csv,
            mimetype="text/csv",
            headers={"Content-Disposition": f"attachment;filename=ad_campaign_{product[:20]}.csv"}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/export/notion", methods=["POST", "OPTIONS"])
def export_notion():
    if request.method == "OPTIONS":
        return jsonify({}), 200
    try:
        data    = request.json
        product = data.get("product", "")
        audience= data.get("audience", "")
        tone    = data.get("tone", "")
        results = data.get("results", {})
        md      = results_to_notion(product, audience, tone, results)
        return jsonify({"markdown": md})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/history", methods=["GET"])
def get_history():
    try:
        if not os.path.exists("history.json"):
            return jsonify([])
        with open("history.json", "r") as f:
            history = json.load(f)
        return jsonify(list(reversed(history[-20:])))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)