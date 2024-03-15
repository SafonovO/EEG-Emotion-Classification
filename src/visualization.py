import numpy as np
import matplotlib.pyplot as plt
import PIL as imaging

sensors_angle = []
sensors_radius =[]
with open('src/Data/SEED-IV/channel_62_pos.locs','r') as file:
    for line in file:
        words = line.split()
        print(words)
        sensors_angle.append(np.deg2rad(float(words[1])))
        sensors_radius.append(float(words[2]))


img = plt.imread("src/Data/human-brain-1443447004ROS-1446891627.jpg")
fig, ax = plt.subplots(figsize=(6,6))

img_height, img_width = img.shape[:2]

# Scale the coordinates


ax.imshow(img,aspect='equal')

x = (sensors_radius * np.cos(sensors_angle)) * (img_width-100) - img_width/2
y = (sensors_radius * np.sin(sensors_angle)) * (img_height-100) + img_height/2
rotation_matrix = np.array([[0, 1], [-1, 0]])
rotated_points = np.dot(rotation_matrix, [x,y])
x = rotated_points[0]
y= rotated_points [1]

plt.scatter(x, y, color='r')
ax.axis('off')
plt.show()