import numpy as np
import matplotlib.pyplot as plt
from init import initialize
from forward import forward
from back import backward
from dataset import dataset
from decision import decision
from predict import predict


np.random.seed(0)

# Load the dataset
out = dataset()
X, y = out['X'], out['y']

# Set up the Neural Net
nn_input_dim = X.shape[1]   # input dimension
nn_hdim = 3                 # number of hidden variables
nn_output_dim = 2           # two classes

# Initial model
model = initialize(nn_input_dim, nn_hdim, nn_output_dim)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.show()
fig.canvas.draw()

# Train a model
reg_lambda = 0.01
epsilon = 0.01
num_passes = 1000
for i in range(0, num_passes):
    out = forward(model, X, y)
    z1, a1, probs, yhat = out['z1'], out['a1'], out['probs'], out['yhat']
    model = backward(model, X, y, probs, a1, reg_lambda, epsilon)

    if i % 20 == 0:
        # Plot the contour and training examples
        out = decision(X, y, lambda x: predict(model, x))
        xx, yy, Z = out["xx"], out["yy"], out["Z"]

        ax.clear()
        ax.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
        ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
        plt.pause(0.1)
