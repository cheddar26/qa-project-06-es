import requests
import configuration
import data



def creation_new_user(namenw):
    json_body_new_user = information_new_usser(namenw)
    json_body_new_user_response = post_new_user(json_body_new_user)
    assert json_body_new_user_response.status_code == 201,"No se creó el usuario."
    assert json_body_new_user_response.json()["authToken"] != "","No generó token."
    tkn = json_body_new_user_response.json()
    tab_nwuser = get_created_user()
    str_user = json_body_new_user["firstName"] + "," + json_body_new_user["phone"] + "," \
               + json_body_new_user["address"] + ",,," + tkn["authToken"]
    assert tab_nwuser.text.count(str_user) == 1
    return tkn
def information_new_token(name):
    change_name_token = data.body_new_kit.copy()
    change_name_token["name"] = name
    return change_name_token

def change_headers_authorization(token):
    change_tipe_header = data.headers.copy()
    change_tipe_header["Authorization"]= f"Bearer {token}"
    return change_tipe_header

def information_new_usser(name):
    change_name_user = data.body_new_user.copy()
    change_name_user["firstName"] = name
    return change_name_user

def get_created_user():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kit_body,
                         headers = auth_token)

