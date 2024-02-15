import requests
import sender_stand_request

def positive_assert_nu(namenw):
    j_body = sender_stand_request.inf_nwuser(namenw)
    j_body_resp = sender_stand_request.new_user(j_body)
    print(j_body_resp.status_code)
    assert j_body_resp.status_code == 201,"No se creó el usuario."
    print("El usuario se creó correctamente, código: ",j_body_resp)
    assert j_body_resp.json()["authToken"] != "","No generó token."
    tkn = j_body_resp.json()
    print("El token generado es: ",tkn)
    tab_nwuser = sender_stand_request.created_user()
    str_user = j_body["firstName"] + "," + j_body["phone"] + "," \
               + j_body["address"] + ",,," + tkn["authToken"]
    assert tab_nwuser.text.count(str_user) == 1
    print(tab_nwuser.text)
    return tkn


def nw_kit(name_kit,namenw):
    print("El nombre del nuevo kit ingresado  es: " + name_kit)
    kit_body = sender_stand_request.inf_nwtokn(name_kit)
    response_tokn = sender_stand_request.post_new_kit(kit_body,namenw)
    assert response_tokn.status_code == 201,"No se creó el kit"
    print("El kit se creó correctamente")
    print("El nombre del kit es: " + response_tokn.json()["name"])
    assert response_tokn.json()["id"] != 1,"No se creó el kit"
    tab_Kit_json = response_tokn.json()
    name = tab_Kit_json["name"] if tab_Kit_json["name"] is not None else ""
    products_list = tab_Kit_json["productsList"] if tab_Kit_json["productsList"] is not None else ""
    kit_id = str(tab_Kit_json["id"]) if tab_Kit_json["id"] is not None else ""
    products_count = str(tab_Kit_json["productsCount"]) if tab_Kit_json["productsCount"] is not None else ""

    str_kit = "name: " + name + ","+" products List: " + products_list + " , " +" id: "+ kit_id + " , " +" products count: "+ products_count
    print(str_kit)

def nw_kit_assert_400(name_kit,namenw):
    print("El nombre del nuevo kit ingresado  es: ", name_kit)
    kit_body = sender_stand_request.inf_nwtokn(name_kit)
    response_tokn = sender_stand_request.post_new_kit(kit_body,namenw)
    print("El estado del response es:", response_tokn.status_code)
    assert response_tokn.status_code == 400," No se creó el kit"
    print(response_tokn.status_code)
    assert response_tokn.json()["code"] == 400,"No se creó el kit"
    assert response_tokn.json()["menssage"] == ("No se han aprobado todos los parámetros requeridos")





tookn = positive_assert_nu("Monica")


def test_create_kit_1_caracter():
    print("\n Prueba 1 el número permitido de caracteres (1)")
    nw_kit("Ac", tookn)

def test_create_kit_511_caracters():
    print("\n Prueba 2 el número permitido de caracteres (511)")
    nw_kit("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
           "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
           "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
           "dabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
           "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
           "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
           "abcdabcdabcdabcdabC",tookn)
def test_create_kit_0_caracter():
    print("\n Prueba 3 el número de caracteres es menor que la cantidad permitida (0)")
    nw_kit_assert_400("",tookn)

def test_not_created_kit_512_caracteres():
    print("\n Prueba 4 el número de caracteres es mayor que la cantidad permitida (512)")
    nw_kit_assert_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                      "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                      "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                      "bcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                      "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                      "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",tookn)

def test_created_kit_special_caracters():
    print("\n Prueba 5 se permiten caracteres especiales")
    nw_kit("№%@,",tookn)

def test_created_kit_with_gap():
    print("\n Prueba 6 se permite la creacion de kit con espacios")
    nw_kit("A Aaa ",tookn)

def test_created_kit_with_numbers():
    print("\n Prueba 7 se permite la creacion de kit con numeros")
    nw_kit("123",tookn)

def test_not_created_kit_without_parameter():
    print("\nPrueba 8 El parámetro en la solicitud: kit_body = { }")
    nw_kit_assert_400({},tookn)

def test_not_created_kit_with_another_parameter():
    print("\nPrueba 9 Se ha pasado un tipo de parámetro diferente (número): kit_body = { ""name"": 123 }")
    nw_kit_assert_400({"name":123},tookn)

