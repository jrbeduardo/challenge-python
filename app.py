from flask import Flask, jsonify, render_template, request
from challenge import Challenge 

app = Flask(__name__)

adj_matrix2 = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]
challenge = Challenge(adj_matrix2)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template(
      "index.html", 
      num_nodes = challenge.num_nodes-1,
      matrix = adj_matrix2,
      nodes = challenge.nodes 
    )
@app.route("/adjacent", methods=["POST"])
def adjacent():
    return jsonify(
        {
          "msg": challenge.are_adj(
              int(request.form["node1"]),
              int(request.form["node2"])
              )
        }
    )
    
if __name__ == "__main__":
    app.run(debug=True)
