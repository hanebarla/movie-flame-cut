import os
import glob
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--imgdir", default=".")
parser.add_argument("--interval", default=1, type=int)

args = parser.parse_args()

interval = args.interval
img_list = os.listdir(args.imgdir)
num = len(img_list)
num_order = len(str(num))

all_path = []

for i in range(num-2):
    if (i+2)*interval > (num - 1):
        break
    img_path = {}
    img_path["prev"] = os.path.join(args.imgdir, "demo_{}.png".format(str(i*interval).zfill(num_order)))
    img_path["now"] = os.path.join(args.imgdir, "demo_{}.png".format(str((i+1)*interval).zfill(num_order)))
    img_path["next"] = os.path.join(args.imgdir, "demo_{}.png".format(str((i+2)*interval).zfill(num_order)))

    all_path.append(img_path)

with open("movie_data.json", "w") as f:
    json.dump(all_path, f)
