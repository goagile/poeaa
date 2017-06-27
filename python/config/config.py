import json


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
        cls = type.__new__(mcs, name, bases, class_dict)
        register_class(cls)
        return cls


class Field(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __getattr__(self, item):
        attr = self.kwargs.get(item, None)
        if attr:
            return attr
        return self.__getattribute__(item)

    def __eq__(self, other):
        return all(self.kwargs[key] == other.kwargs[key] for key in self.kwargs.keys())


class Config(object, metaclass=Meta):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __getattr__(self, item):
        attr = self.kwargs.get(item, None)
        if attr:
            return attr
        return self.__getattribute__(item)

    def __eq__(self, other):
        return all(self.kwargs[key] == other.kwargs[key] for key in self.kwargs.keys())

    def get(self, name):
        field = self._find_field(name)
        if field and self._is_field(field):
            return field
        return self.__getattribute__(name)

    @classmethod
    def parse_json(cls, path):
        dict_ = cls._dict_from_json(path)
        for class_name, fields_list in dict_.items():
            fields = {}
            for field_dict in fields_list:
                name = field_dict.get('name')
                fields[name] = Field(**field_dict)
            target_class = registry[class_name]
            result = target_class(**fields)
        return result

    @classmethod
    def _dict_from_json(cls, path):
        result = {}
        with open(path, 'r') as file:
            result = json.load(file)
        return result

    def export_json(self, path):
        result = {self.__class__.__name__: [field.kwargs for field in self.kwargs.values()]}
        with open(path, 'w') as file:
            json.dump(result, fp=file, ensure_ascii=False)

    def _find_field(self, name):
        field = self.kwargs.get(name, None)
        if field and self._is_field(field):
            return field
        else:
            return self.__dict__.get(name, None)

    @classmethod
    def _is_field(cls, field):
        return isinstance(field, Field)

    def generate_py_file(self, path):
        import_string = 'from examples.python.config.config import Config, Field'

        class_template = (
"""
{import_string}


class {config_name}(Config):
{fields}
"""
        )

        field_template = ("   {name} = Field(label='{label}')")

        fields = ''
        for f in self.kwargs.values():
            fields += field_template.format(name=f.name, label=f.label) + '\n'

        gen = class_template.format(
            import_string=import_string,
            config_name=self.__class__.__name__,
            fields=fields
        )

        with open(path, 'w') as file:
            file.write(gen)
