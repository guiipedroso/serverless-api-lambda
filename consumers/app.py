from chalice import Chalice

app = Chalice(app_name='consumers')

users = {
           "users": [
                {"name": "usuario1", "phone": "679999999"},
                {"name": "usuario2", "phone": "679999998"},
                {"name": "usuario3", "phone": "679999997"},
                {"name": "usuario4", "phone": "679999996"},
            ]
        }

companies = {
                "companies": [
                    {"name": "empresa1", "phone": "679999995"},
                    {"name": "empresa2", "phone": "679999994"},
                    {"name": "empresa3", "phone": "679999993"},
                    {"name": "empresa4", "phone": "679999992"},
                ]
            }

@app.route('/consumers/person', methods=['POST'])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "status": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response

@app.route('/consumers/person', methods=['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    response = {
        "status": 200,
        "body": f"Usuário {requests_params} atualizado com sucesso!"
    }
    return response

@app.route('/consumers/person', methods=['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "status": 200,
        "body": f"Usuário {requests_params} deletado com sucesso!"
    }
    return response

@app.route('/consumers/persons', methods=['GET'])
def get_persons():
    response = {
        "status": 200,
        "body": users
    }
    return response


@app.route('/consumers/person/{id}', methods=['GET'])
def get_person(id):
    response = {
        "status": 200,
        "body": {id: {"name": "usuario1", "phone": "679999999"}}
    }
    return response


@app.route('/consumers/company', methods=['POST'])
def create_company():
    requests_params = app.current_request.json_body
    response = {
        "status": 200,
        "body": f"Empresa {requests_params} criada com sucesso!"
    }
    return response

@app.route('/consumers/company', methods=['PUT'])
def update_company():
    requests_params = app.current_request.json_body
    response = {
        "status": 200,
        "body": f"Empresa {requests_params} atualizada com sucesso!"
    }
    return response

@app.route('/consumers/company', methods=['DELETE'])
def delete_company():
    requests_params = app.current_request.json_body
    response = {
        "status": 200,
        "body": f"Empresa {requests_params} removida com sucesso!"
    }
    return response

@app.route('/consumers/companies', methods=['GET'])
def get_companies():
    response = {
        "status": 200,
        "body": companies
    }
    return response

@app.route('/consumers/companies/{id}', methods=['GET'])
def get_company(id):
    response = {
        "status": 200,
        "body": {id: {"name": "empresa1", "phone": "679999995"}}
    }
    return response
