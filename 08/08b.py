#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

img_data = lines[0].strip()

width = 25
height = 6

pixels_per_layer = width * height
img_data_len = len(img_data)
layer_count = img_data_len // pixels_per_layer

layers = []
for l in range(layer_count):
    layer = []
    for i in range(height):
        layer.append([None])
    layers.append(layer)

for i in range(layer_count):
    layer_data = img_data[i * pixels_per_layer: (i+1) * pixels_per_layer]
    
    row = 0
    for j in range(height):
        row_data = layer_data[j * width: (j+1) * width]
        layers[i][row] = row_data
        row += 1

full_img = [[None] * width for i in range(height)]

for i in range(width):
    for j in range(height):
        for z in range(layer_count):
            #print(layers[z][j][i])
            if layers[z][j][i] in ('0','1'):
                full_img[j][i] = layers[z][j][i]
                break

for j in range(height):
    print(''.join(full_img[j]).replace('1','*',).replace('0',' '))
