import os

path = os.path.join(os.sep, os.getcwd(), 'val')
file = open(os.path.join(os.sep, path, 'val_annotations.txt'), 'r')
dir2image = {}
for line in file:
    image = line[0:line.find('\t')]
    dir = line[line.find('\t')+1:line.find('\t', line.find('\t') + 1)]
    dir2image[dir].append(image)
