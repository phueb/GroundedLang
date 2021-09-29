from groundedlang.workspace import WorkSpace as Ws


def match_arg_y_name(arg_y_name: str):
    if arg_y_name == Ws.Y.name:
        return True
    return False


def match_arg_y_category(arg_y_name: str):
    if arg_y_name == Ws.Y.category:
        return True
    return False
