def all_thing_is_obj(object: any) -> int:
    match (type(object)):
        case isinstance(object, list):
            print("List : ", type(object))
        case isinstance(object, set):
            print("Set : ", type(object))
        case isinstance(object, dict):
            print("Dict : ", type(object))
        case isinstance(object, tuple):
            print("Tuple : ", type(object))
        case isinstance(object, str):
            print("Brian : ", type(object))
        case _:
            print("Type not found")
    return 42