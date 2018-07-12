import sklearn
import sklearn.datasets


def dataset():
    X, y = sklearn.datasets.make_moons(200, noise=0.20)
    return {"X": X, "y": y}
