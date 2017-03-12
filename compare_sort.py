import random
import datetime
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode()

from . import selectionsort
from . import insertionsort
from . import mergesort
from . import bubblesort


def compare_sort_functions(functions, names, from_size, to_size, a, b):
    traces = []
    X = [size for size in range(from_size, to_size+1)]
    Y = [[] for f in functions]

    for size in X:
        A = [random.randint(a, b) for i in range(size)]
        to_sort = [A[:] for f in functions]
        for i, f in enumerate(functions):
            start = datetime.datetime.now()
            f(to_sort[i])
            end = datetime.datetime.now()
            Y[i].append((end-start).total_seconds())

    for i, f in enumerate(functions):
        traces.append(
            go.Scatter(
                x=X,
                y=Y[i],
                name=names[i]
            )
        )

    return py.plot(traces)


def run():
    functions = [selectionsort.sort, insertionsort.sort, mergesort.sort, bubblesort.sort]
    names = ['selection', 'insertion', 'merge', 'bubble']
    rest = [0, 1000, -1000, 1000]
    compare_sort_functions(functions, names, *rest)
