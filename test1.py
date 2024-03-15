dic = {"a": "3rfdf", "b": [1, 2, 4], "c": 4, "d": {"d1": 65, "d2": [23, 89, "4r"]}}



for k, v in dic.items():
    if isinstance(v, dict):
        print(k)
        for k1, v1 in v.items():
            print(k1)
    else:
        print(k)


