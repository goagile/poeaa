import json


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
        cls = type.__new__(mcs, name, bases, class_dict)
        return cls


class Field(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __getattr__(self, item):
        attr = self.kwargs.get(item, None)
        if attr:
            return attr
        return self.__getattribute__(item)


class Config(metaclass=Meta):

    def __init__(self):
        pass

    @classmethod
    def load(cls, path):
        print('Try to import')
        result = {}
        with open(path, 'r') as file:
            result = json.load(file)

        instance = Config()
        for k, v in result.items():
            setattr(instance, k, Field(**{k: v}))

        return instance
