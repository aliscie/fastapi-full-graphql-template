def list_filter(x, data=None,operator='and',search=None):
    import re
    y = []
    keys = []
    try:
        keys = x[0].__dict__.keys()
    except:
        pass

    if search:
        for i in x:
            is_ = []
            for key in keys:
                is_.append(str(getattr(i,key)).lower().__contains__(str(search).lower()))
            if any(is_):
                y.append(i)
    elif data:
        for i in x:
            is_ = []
            for key, value in data.items():
                v = re.search(r'(__.+__)', key)
                key = re.sub(r'__.+__', '', key)

                attr_ = getattr(i, key)
                if v:
                    is_.append(getattr(attr_, v.group(1))(value))
                else:
                    is_.append(attr_.__eq__(value))

            #  append values based on the condition met.
            if operator == 'and':
                if all(is_):
                    y.append(i)
            elif operator == 'or':
                if any(is_):
                    y.append(i)
            elif operator == 'not':
                if not is_[0]:
                    y.append(i)
    else:
        return x
    return y