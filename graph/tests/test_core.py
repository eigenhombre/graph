from graph.core import *

def test_fninputs():
    def f(x, y):
        return x + y
    assert fninputs(f) == ('x', 'y')

def test_run():
    dag = {'a': lambda x, y: x + y,
           'm': lambda x, y: x * y,
           'result': lambda a, m: max(a, m),
           'not_run': lambda m, x, result: 1/0}

    ins = {'x': 1,  'y': 2}

    assert run(dag, ins, ('result',)) == (3,)
    assert run(dag, ins, ('a', 'm', 'result')) == (3, 2, 3)

def test_prismatic_example():
    dag = {'n': lambda xs: len(xs),
           'm': lambda xs, n: float(sum(xs)) / n,
           'm2': lambda xs, n: float(sum([x*x for x in xs])) / n,
           'v': lambda m, m2: (m2 - m * m)}

    ins = {'xs': [1, 2, 3, 4, 5]}

    assert run(dag, ins, ('v',)) == (2,)
