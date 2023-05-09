import numpy as np
import matplotlib.pyplot as plt
from skimage import data, io, segmentation, color
from skimage.future import graph

# Load an image
image = data.coffee()

# Perform segmentation on the image
labels = segmentation.slic(image, compactness=30, n_segments=400)

# Compute the region adjacency graph of the segmented image
g = graph.rag_mean_color(image, labels)

# Merge small regions based on color similarity
labels2 = graph.cut_threshold(labels, g, 30)

# Color the segmented regions with random colors
out = color.label2rgb(labels2, image, kind='avg')

# Display the original and segmented images
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ax[0].imshow(image)
ax[0].set_title('Original')
ax[1].imshow(out)
ax[1].set_title('Segmented')
plt.show()
