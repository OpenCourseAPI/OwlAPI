def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
