import requests
import configuration
import data

def inf_nwtokn(name):
    ch_name = data.body_kit.copy()
    ch_name["name"] = name
    return ch_name

def inf_nwuser(name):
    ch_name = data.N_user.copy()
    ch_name["firstName"] = name
    return ch_name

def created_user():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_kit(kit_body,auth_token):
    headers = {
        'Authorization': 'Bearer '+ auth_token['authToken']
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kit_body,
                         headers = headers)

