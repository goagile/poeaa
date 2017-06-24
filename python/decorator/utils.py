

def prop(name, validate, doc=None):
    protected_name = '_' + name

    def decorator(instance):
        def getter(instance):
            return getattr(instance, protected_name)

        def setter(instance, value):
            validate(instance, protected_name, value)
            setattr(instance, protected_name, value)
        setattr(instance, name, property(getter, setter, doc=doc))
        return instance

    return decorator


def is_in_range(minimum=10, maximum=100):
    message = 'Поле {class_name}.{name} = {value} вне диапазона ({minimum};{maximum})'
    def is_in_range(instance, name, value):
        class_name = instance.__class__.__name__
        if not minimum <= value <= maximum:
            raise ValueError(message.format(**locals()))
    return is_in_range
