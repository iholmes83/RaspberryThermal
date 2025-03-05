from flask import Flask, request, jsonify, send_from_directory
import json
import os
import requests 

app = Flask(__name__)

LIST_FILE = "shopping_list.json"

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/save_list", methods=["POST"])
def save_list():
    try:
        data = request.get_json()
        print("Data received:", data)  # Debug

        if not data or "items" not in data:
            print("❌ Error: no data!")
            return jsonify({"error": "no data!"}), 400

        with open(LIST_FILE, "w", encoding="utf-8") as file:
            json.dump(data["items"], file, indent=4)

        print("✅ List saved:", data["items"])
        return jsonify({"message": "List saved"})

    except Exception as e:
        print("❌ Error saving:", e)
        return jsonify({"error": str(e)}), 500

@app.route("/get_list", methods=["GET"])
def get_list():
    if os.path.exists(LIST_FILE):
        with open(LIST_FILE, "r", encoding="utf-8") as file:
            items = json.load(file)
        return jsonify(items)
    return jsonify([])

@app.route("/clear_list", methods=["POST"])
def clear_list():
    if os.path.exists(LIST_FILE):
        os.remove(LIST_FILE)
    return jsonify({"message": "List deleted!"})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# IP e Porta del ServerRecieve
PRINT_SERVER_URL = "http://127.0.0.1:5005/print" #You can set here a different address if the webserver and the printer are in separate places

@app.route("/print", methods=["POST"])
def print_list():
    try:
        data = request.get_json(force=True)
        if not data or "list" not in data:
            return jsonify({"error": "No list!"}), 400
        
        list_text = data["list"]

        # Invia la richiesta a ServerRecieve.py
        response = requests.post(PRINT_SERVER_URL, json={"list": list_text})
        
        if response.status_code == 200:
            return jsonify({"Info": "List Sent"})
        else:
            return jsonify({"Error": f"Error of the printer: {response.text}"}), response.status_code

    except Exception as e:
        print("❌ Error printing:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083)
