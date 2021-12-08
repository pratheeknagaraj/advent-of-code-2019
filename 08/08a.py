#!/usr/bin/python3

with open('08_input', 'r') as f:
    lines = f.readlines()

img_data = lines[0].strip()

width = 25
height = 6

pixels_per_layer = width * height
img_data_len = len(img_data)
layer_count = img_data_len // pixels_per_layer

fewest_zeros = float('inf')
val = None

for i in range(layer_count):
    layer_data = img_data[i * pixels_per_layer: (i+1) * pixels_per_layer]
    zeros = layer_data.count('0')
    ones = layer_data.count('1')
    twos = layer_data.count('2')

    if zeros < fewest_zeros:
        fewest_zeros = zeros
        val = ones * twos

print(val)
