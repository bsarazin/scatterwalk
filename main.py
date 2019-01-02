import matplotlib.pyplot as plt 
from random_walk import Randomwalk

while True:
    # Make a random walk and then plot the points
    rw = Randomwalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(figsize=(10,6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)

    # Highlight first and last points
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],c='red',edgecolors='none',s=100)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Run again [y/n]')
    if keep_running == 'n':
        break