from chalice import Chalice

app = Chalice(app_name='sales')

sales = {
            "sales": [
                {"consumer": "usuário1", "value": "12,50", "food": "pizza"},
                {"consumer": "usuário2", "value": "11,80", "food": "estrogonofe"},
                {"consumer": "usuário3", "value": "10,90", "food": "macarronada"},
            ]
        }


@app.route('/sales/offline', methods = ['POST'])
def create_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} criada com sucesso!"
    }
    return response


@app.route('/sales/offline',  methods=['PUT'])
def update_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} atualizada com sucesso!"
    }
    return response


@app.route('/sales/offline',  methods=['DELETE'])
def delete_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} deletada com sucesso!"
    }
    return response


@app.route('/sales/offlines',  methods=['GET'])
def get_sales():
    response = {
        "statusCode": 200,
        "body": sales
    }
    return response


@app.route('/sales/offline/{id}',  methods=['GET'])
def get_sale(id):
    response = {
        "statusCode": 200,
        "body": {id: {"consumer": "usuário1", "value": "12,50", "food": "pizza"}}
    }
    return response


@app.route('/sales/online',  methods=['POST'])
def create_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} criada com sucesso!"
    }
    return response


@app.route('/sales/online',  methods=['PUT'])
def update_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} atualizada com sucesso!"
    }
    return response


@app.route('/sales/online',  methods=['DELETE'])
def delete_sale():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Venda {requests_params} deletada com sucesso!"
    }
    return response


@app.route('/sales/onlines',  methods=['GET'])
def get_sales():
    response = {
        "statusCode": 200,
        "body": sales
    }
    return response


@app.route('/sales/online/{id}',  methods=['GET'])
def get_sale(id):
    response = {
        "statusCode": 200,
        "body": {id:  {"consumer": "usuário1", "value": "12,50", "food": "pizza"}}
    }
    return response