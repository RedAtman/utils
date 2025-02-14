class _Singleton(type):
    """单例模式(保证条件符合的对象仅被创建一次)

    Args:
        type (_type_): _description_

    Returns:
        _type_: _description_
    """

    _map = dict()

    def __call__(cls, *args, **kwargs):
        print("__call__", cls, *args, **kwargs)
        _id = args[0]
        ist = cls._map.get(_id)
        if ist is None:
            print("if ist is None:", ist, super(_Singleton, cls))
            ist = super().__call__()
            cls._map[_id] = ist
            return ist
        return cls._map[_id]

    def __new__(cls, *args, **kwargs):
        print("__new__", cls, *args, **kwargs)
        return super().__new__(cls, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("__init__", cls, *args, **kwargs)
        return super().__init__(*args, **kwargs)


class _Point(
    # object,
    metaclass=_Singleton,
):
    pass


if __name__ == "__main__":

    obj = _Point(1)
    obj1 = _Point(1)
    obj2 = _Point(2)
    assert obj is obj1
    assert obj is not obj2
    print(obj, obj1, obj2)
