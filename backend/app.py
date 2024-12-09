from flask import Flask, jsonify, request
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time

from service import query

app = Flask(__name__)

REQUEST_COUNT = Counter('app_request_count', 'Total request count', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['method', 'endpoint'])

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {'/metrics': make_wsgi_app()})

@app.route('/query', methods=['GET'])
def get_recipes():

    start_time = time.time()

    username = request.args.get('username')

    #print(f"Received username for query: {username}")

    if not username:
        REQUEST_COUNT.labels('GET', '/query', 400).inc()
        REQUEST_LATENCY.labels('GET', '/query').observe(time.time() - start_time)
        return jsonify({"error": "Username is required"}), 400
    
    
    result = query(username)

    REQUEST_COUNT.labels('GET', '/query', 200).inc()
    REQUEST_LATENCY.labels('GET', '/query').observe(time.time() - start_time)

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
