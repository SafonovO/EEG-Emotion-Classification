import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke
def visualize_frame(sensors_values):
    sensors_angle = []
    sensors_radius = []

    with open('src/Data/SEED-IV/channel_62_pos.locs', 'r') as file:
        for line in file:
            words = line.split()
            sensors_angle.append(np.deg2rad(float(words[1])))
            sensors_radius.append(float(words[2]))

    img = plt.imread("src/Data/human-brain-1443447004ROS-1446891627.jpg")
    fig, ax = plt.subplots(figsize=(7, 8))

    img_height, img_width = img.shape[:2]

    ax.imshow(img, aspect='equal')

    x = (sensors_radius * np.cos(sensors_angle)) * (img_width - 150) - img_width / 2
    y = (sensors_radius * np.sin(sensors_angle)) * (img_height - 150) + img_height / 2
    rotation_matrix = np.array([[0, 1], [-1, 0]])
    rotated_points = np.dot(rotation_matrix, [x, y])
    x = rotated_points[0]
    y = rotated_points[1]

    # Create a color map based on sensor values
    
    color_map = plt.cm.jet  # You can change the colormap as needed
    
    sc = ax.scatter(x, y, c=sensors_values, cmap=color_map,s=120)
    ax.axis('off')
    ax.set_title("Mean Amplitude")
    # Add a colorbar without normalization
    cbar = plt.colorbar(sc, ax=ax, ticks=np.linspace(sensors_values.min(), sensors_values.max(), num=5))
    cbar.set_label('Sensor Values', fontsize=12)

    outline_effect = [withStroke(linewidth=2, foreground="black")]

    # Add sensor numbers as annotations
    for i, (x_coord, y_coord) in enumerate(zip(x, y)):
        ax.annotate(str(i + 1), (x_coord, y_coord), color="white", fontsize=8, ha='center', va='center',
                    path_effects=outline_effect)

    
        
    return fig