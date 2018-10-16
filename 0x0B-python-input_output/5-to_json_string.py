#!/usr/bin/python3
def to_json_string(my_obj):
    import json
    try:
        json.dumps(my_obj)
        return str(my_obj)
    except:
        raise TypeError("{} is not JSON serializable".format(my_obj))
