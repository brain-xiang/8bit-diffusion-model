"""
This script visualizes a set of images stored in a NumPy array using matplotlib.
The script allows the user to navigate through the images using Next and Previous buttons,
and also provides an input box to directly jump to a specific image index.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.widgets import Button, TextBox

workspace_path = Path.cwd()

# Change the path to the model you want to visualize
# data = np.load(workspace_path / "data" / "sprites_1788_16x16.npy")
data = np.load(workspace_path / "generations" / "1000_generations.npy")

fig, axes = plt.subplots(8,8, figsize=(15,15))
plt.subplots_adjust(bottom=0.1, hspace=0.4)

current_index = 0
for i, ax in enumerate(axes.flat):
    ax.imshow(data[i])
    current_index = i
    ax.set_title(f"Image {current_index}")

def next_images(event):
    global current_index
    for i, ax in enumerate(axes.flat):
        current_index += 1
        ax.imshow(data[current_index])
        ax.set_title(f"Image {current_index}")
    plt.title(f"Showing Images: {current_index - len(axes.flat)} - {current_index}")
    plt.draw()
    
def prev_images(event):
    global current_index
    current_index = max(-1, current_index - len(axes.flat)*2)
    next_images(event)

def update_index(text):
    global current_index
    current_index = int(text) - 1
    next_images(None)

# Create button axes
next_ax = plt.axes([0.81, 0.05, 0.1, 0.03])
prev_ax = plt.axes([0.7, 0.05, 0.1, 0.03])  # [left, bottom, width, height]
input_ax = plt.axes([0.1, 0.05, 0.5, 0.03])

# Create buttons
btn_next = Button(next_ax, 'Next')
btn_prev = Button(prev_ax, 'Previous')
text_box = TextBox(input_ax, 'Index:', initial=f"{current_index}")

# Connect buttons to callback functions
btn_next.on_clicked(next_images)
btn_prev.on_clicked(prev_images)
text_box.on_submit(update_index)

plt.title(f"Showing Images: {current_index - len(axes.flat)} - {current_index}")
plt.show()