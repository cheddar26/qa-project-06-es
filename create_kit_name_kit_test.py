import requests
import data
import sender_stand_request

def validate_new_kit_response_201(name_kit,usser_token):
    kit_body = sender_stand_request.information_new_token(name_kit)
    headers_body = sender_stand_request.change_headers_authorization(usser_token)
    response_tokn = sender_stand_request.post_new_kit(kit_body,headers_body)
    assert response_tokn.status_code == 201,"No se creó el kit"
    assert response_tokn.json()["name"] == name_kit,"No se creó el kit"

def validate_new_kit_response_400(name_kit,usser_token):
    kit_body = sender_stand_request.information_new_token(name_kit)
    headers_body = sender_stand_request.change_headers_authorization(usser_token)
    response_tokn = sender_stand_request.post_new_kit(kit_body,headers_body)
    assert response_tokn.status_code == 400," No se creó el kit"
    assert response_tokn.json()["code"] == 400,"No se creó el kit"
    assert response_tokn.json()["menssage"] == ("No se han aprobado todos los parámetros requeridos")

token_created_new_user = sender_stand_request.creation_new_user("Navor")


def test_create_kit_1_characters():
    validate_new_kit_response_201(data.one_character, token_created_new_user)

def test_create_kit_511_characters():
    validate_new_kit_response_201(data.five_hundred_eleven_characters,token_created_new_user)
def test_create_kit_0_characters():
    validate_new_kit_response_400(data.zero_character,token_created_new_user)

def test_not_created_kit_512_ccharacters():
    validate_new_kit_response_400(data.five_hundred_twelve_characters,token_created_new_user)

def test_created_kit_special_characters():
    validate_new_kit_response_201(data.special_characters,token_created_new_user)

def test_created_kit_with_gap():
    validate_new_kit_response_201(data.characteres_with_gap,token_created_new_user)

def test_created_kit_with_numbers():
    validate_new_kit_response_201(data.numeric_characters,token_created_new_user)

def test_not_created_kit_without_parameter():
    validate_new_kit_response_400(data.without_parameter,token_created_new_user)

def test_not_created_kit_with_another_parameter():
    validate_new_kit_response_400(data.another_parameter,token_created_new_user)

