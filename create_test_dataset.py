import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
# Model configuration.
parser.add_argument('--data', type=str, default='data', help='path to dataset')
parser.add_argument('--n_samples', type=int, default=10, help='number of samples to be chosen')
config = parser.parse_args()

path = config.data
names = np.array(os.listdir(path))
np.random.shuffle(names)
names = names[:config.n_samples]

f = open('males_image_list.txt', 'w')
for name in names:
  img_path = path + '/' + name
  f.write(img_path)
  f.write('\n')
f.close()   
