import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Assuming data is a 4D numpy array with shape (C, D, H, W)
data = np.random.rand(1, 64, 128, 128)  # Example data

fig, ax = plt.subplots()

def update(frame):
    ax.imshow(data[0, frame, :, :], cmap='gray')
    ax.set_title(f'Slice {frame}')

ani = FuncAnimation(fig, update, frames=data.shape[1], repeat=False)
plt.show()