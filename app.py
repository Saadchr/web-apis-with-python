from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/greet")
def index():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    if not fname and not lname:
        return jsonify({"status":"error"})
    elif not fname and lname:
        response = {"data": f"Hello, mr {lname}"}
    
    elif not lname and fname:
        response = {"data": f"Heyyy, {fname}"}
    elif lname and fname:
        response = {"data": f"Is that you, {fname} {lname}"}

    
    return jsonify(response)