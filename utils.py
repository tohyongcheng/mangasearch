def strip_jsonp_to_json(jsonp):
    l_index = jsonp.index('(') + 1
    r_index = jsonp.rindex(')')
    res = jsonp[l_index:r_index]

    return res