def NULL_not_found(object: any) -> int
    match type(object):
        case None:
            print("Nothing: ", object, type(object))
        case int:
            print("Zero: ", object, type(object))
        case bool:
            print("Fake: ", object, type(object))
        case float:
            print("Cheese: " object, type(object))
        case str and len(object) < 1:
            print("Empty: " type(object))
        case _:
            print("Type not found")
            return 1
        return 0