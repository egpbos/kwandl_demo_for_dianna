# DIANNA "EXPLAIN" API IN A NUTSHELL:

class SomeXAIMethod:
    def __init__(self, some_parameter='something'):
        ...

    def explain(self, model, data, something='!'):
        print("I did it")


class SomeOtherXAIMethod:
    def __init__(self, other_parameter='default'):
        ...

    def explain(self, model, data, otherwise=None):
        print("I did other things")


methods = {
    'some': SomeXAIMethod,
    'other': SomeOtherXAIMethod
}


# SIMPLE, UNIFIED API
def explain(model, data, method, **kwargs):
    explainer = methods[method](**kwargs)
    explainer.explain(model, data, **kwargs)


if __name__ == '__main__':
    # BUT IT DON'T WORK!
    explain(1, 2, 'some', some_parameter='this', something='that')


# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In [1], line 41
#      37     explainer.explain(model, data, **kwargs)
#      40 # BUT IT DON'T WORK!
# ---> 41 explain(1, 2, 'some', some_parameter='this', something='that')

# Cell In [1], line 36, in explain(model, data, method, **kwargs)
#      35 def explain(model, data, method, **kwargs):
# ---> 36     explainer = methods[method](**kwargs)
#      37     explainer.explain(model, data, **kwargs)

# TypeError: __init__() got an unexpected keyword argument 'something'
