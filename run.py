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
#np.random.shuffle(names)
#names = names[:1]

count = 1
for name in names:
  f = open('males_image_list.txt', 'w')
  img_path = path + '/' + name
  f.write(img_path)
  f.write('\n')
  f.close()
  try:
    os.system("CUDA_VISIBLE_DEVICES=0 python test.py --name males_model --which_epoch latest --display_id 0 --traverse --image_path_file males_image_list.txt --in_the_wild --deploy --interp_step 1 --loadSize 512 --fineSize 512")
    print("{} no of images saved".format(count))
    count += 1
  except:
    print("failed on {}".format(name))
    
