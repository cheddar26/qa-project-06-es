import requests
import data
import sender_stand_request

def new_kit(name_kit,usser_token):
    kit_body = sender_stand_request.information_new_token(name_kit)
    headers_body = sender_stand_request.change_headers_authorization(usser_token)
    response_tokn = sender_stand_request.post_new_kit(kit_body,headers_body)
    assert response_tokn.status_code == 201,"No se creó el kit"
    assert response_tokn.json()["name"] == name_kit,"No se creó el kit"
    tab_Kit_json = response_tokn.json()
    name = tab_Kit_json["name"] if tab_Kit_json["name"] is not None else ""
    products_list = tab_Kit_json["productsList"] if tab_Kit_json["productsList"] is not None else ""
    kit_id = str(tab_Kit_json["id"]) if tab_Kit_json["id"] is not None else ""
    products_count = str(tab_Kit_json["productsCount"]) if tab_Kit_json["productsCount"] is not None else ""
    str_kit = "name: " + name + ","+" products List: " + products_list + " , " +" id: "+ kit_id + " , " +" products count: "+ products_count
    print(str_kit)

def nw_kit_assert_400(name_kit,usser_token):
    kit_body = sender_stand_request.information_new_token(name_kit)
    headers_body = sender_stand_request.change_headers_authorization(usser_token)
    response_tokn = sender_stand_request.post_new_kit(kit_body,headers_body)
    print("El estado del response es:", response_tokn.status_code)
    assert response_tokn.status_code == 400," No se creó el kit"
    print(response_tokn.status_code)
    assert response_tokn.json()["code"] == 400,"No se creó el kit"
    assert response_tokn.json()["menssage"] == ("No se han aprobado todos los parámetros requeridos")

tookn = sender_stand_request.creation_new_user("Navor")


def test_create_kit_1_characters():
    new_kit(data.one_character, tookn)

def test_create_kit_511_characters():
    new_kit(data.five_hundred_eleven_characters,tookn)
def test_create_kit_0_characters():
    nw_kit_assert_400(data.zero_character,tookn)

def test_not_created_kit_512_ccharacters():
    nw_kit_assert_400(data.five_hundred_twelve_characters,tookn)

def test_created_kit_special_characters():
    new_kit(data.special_characters,tookn)

def test_created_kit_with_gap():
    new_kit(data.characteres_with_gap,tookn)

def test_created_kit_with_numbers():
    new_kit(data.numeric_characters,tookn)

def test_not_created_kit_without_parameter():
    nw_kit_assert_400(data.without_parameter,tookn)

def test_not_created_kit_with_another_parameter():
    nw_kit_assert_400(data.another_parameter,tookn)

