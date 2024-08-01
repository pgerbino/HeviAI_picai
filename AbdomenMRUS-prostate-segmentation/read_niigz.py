# Load the NIfTI file
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the NIfTI file
# original segmentation
file_path = '/home/piero/Downloads/prostate158/prostate158_train/train/020/t2_anatomy_reader1.nii.gz'
# validation raw for 20
# file_path = '/home/piero/Downloads/uunet/results/nnUNet/3d_fullres/Task2202_prostate_segmentation/nnUNetTrainerV2_Loss_FL_and_CE_checkpoints__nnUNetPlansv2.1/all/validation_raw/020_020.nii.gz'
img = nib.load(file_path)

# Get the image data as a numpy array
data = img.get_fdata()

# Set up the figure and axis
fig, ax = plt.subplots()

# Function to update the image for each frame
def update(slice_index):
    ax.clear()
    ax.imshow(data[:, :, slice_index].T, cmap="gray", origin="lower")
    ax.set_title(f"Slice {slice_index}")

# Create the animation
num_slices = data.shape[2]
anim = FuncAnimation(fig, update, frames=num_slices, interval=100)

# Save the animation
anim.save('nifti_animation.gif', writer='imagemagick')

# plt.show()

