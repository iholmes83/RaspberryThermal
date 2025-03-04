from flask import Flask, request
from flask_cors import CORS
from Adafruit_Thermal import *

app = Flask(__name__)
CORS(app)

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5) #change as needed

@app.route("/print", methods=["POST"])
def print_list():
    data = request.json
    if not data or "list" not in data:
        return "Dati non validi", 400

    messaggio = data["list"]
    
    printer.wake()
    printer.inverseOn()

    printer.justify('C')
    printer.setSize('M')
    printer.println("Shopping list")
    printer.inverseOff()
    printer.justify('L')  # Align Left
    printer.setSize('M')  # Medium
    printer.println(messaggio)
    printer.println('\n')
    printer.sleep()
    printer.setDefault()

    return "Printed", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
