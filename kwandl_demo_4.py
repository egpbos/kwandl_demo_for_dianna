from kwandl_demo_2 import *


def explain(model, data, method, **kwargs):
    our_method_here = methods[method]

    init_kwargs = get_kwargs_applicable_to_function(our_method_here.__init__, kwargs)

    explainer = our_method_here(**init_kwargs)

    explain_kwargs = get_kwargs_applicable_to_function(explainer.explain, kwargs)

    # ONLY AT THIS POINT CAN WE CHECK EVERYTHING
    unexpected_keywords = set(kwargs) - set(init_kwargs) - set(explain_kwargs)
    if unexpected_keywords:
        raise TypeError(f"explain() got an unexpected keyword argument '{unexpected_keywords.pop()}'")

    explainer.explain(model, data, **explain_kwargs)

# AGAIN, ORIGINAL SIMPLE VERSION FOR COMPARISON:

# def explain(model, data, method, **kwargs):
#     explainer = methods[method](**kwargs)
#     explainer.explain(model, data, **kwargs)

if __name__ == '__main__':
    # OK, GOOD, NOW IT FAILS ON WRONG PARAMETERS, AS EXPECTED
    explain(1, 2, 'other', some_parameter='this', something='that')
    # ... BUT THE BOILERPLATE OF OUR ONCE TWO-LINE FUNCTION HAS EXPLODED


