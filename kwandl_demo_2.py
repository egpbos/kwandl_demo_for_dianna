from kwandl_demo_1 import *

# DIANNA SOLUTION:

import inspect

def get_kwargs_applicable_to_function(function, kwargs):
    """Returns a subset of `kwargs` of only arguments and keyword arguments of `function`."""
    return {key: value for key, value in kwargs.items()
            if key in inspect.getfullargspec(function).args}


def explain(model, data, method, **kwargs):
    our_method_here = methods[method]

    init_kwargs = get_kwargs_applicable_to_function(our_method_here.__init__, kwargs)
    explainer = our_method_here(**init_kwargs)

    explain_kwargs = get_kwargs_applicable_to_function(explainer.explain, kwargs)
    explainer.explain(model, data, **explain_kwargs)

# COMPARE TO PREVIOUS, BLISSFULLY SIMPLE VERSION:

# def explain(model, data, method, **kwargs):
#     explainer = methods[method](**kwargs)
#     explainer.explain(model, data, **kwargs)

# OH WELL...

if __name__ == '__main__':
    # ...AT LEAST NOW IT DOES WORK!
    explain(1, 2, 'some', some_parameter='this', something='that')