import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('data.csv')

# Calculate mean and standard deviation of x1 and x2 columns using numpy
x1_mean = np.mean(data['x1'])
x2_mean = np.mean(data['x2'])
# Create a scatter plot of the data
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(data['x1'], data['x2'], data['y'], alpha=0.5)

# Add mean and standard deviation lines to the plot
ax.plot([x1_mean, x1_mean], [x2_mean, x2_mean], 
        [np.min(data['y']), np.max(data['y'])], 
        'r', linestyle='--', label='x1 mean')
ax.legend()

# Add labels and title to the plot
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('Scatter Plot with Mean and Standard Deviation')

# Show the plot
plt.show()

