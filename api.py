from flask import Flask, request, jsonify
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
CONFIG = {'AMQP_URI': "amqp://guest:guest@192.168.99.100"}

@app.route('/', methods=['GET'])
def root():
	return "Hello! I'm a sale management microservice system."

@app.route('/sale/sell/<int:product_id>', methods=['POST'])
def sell(product_id):
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.sale.sell.async(product_id)
        return jsonify({'task': "ok"}), 200

app.run(debug=True)