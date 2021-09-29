from groundedlang.workspace import WorkSpace as Ws


def match_arg_y_name(arg_y_name: str):
    if arg_y_name == Ws.y.name:
        return True
    return False


def match_arg_y_category(arg_y_name: str):
    if arg_y_name == Ws.y.category:
        return True
    return False
