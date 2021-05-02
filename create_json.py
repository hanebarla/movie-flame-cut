import os
import glob
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--imgdir", default=".")

args = parser.parse_args()

img_list = os.listdir(args.imgdir)
num = len(img_list)
num_order = len(str(num))

all_path = []

for i in range(num-2):
    img_path = {}
    img_path["prev"] = os.path.join(args.imgdir, "demo_{}.png".format(str(i).zfill(num_order)))
    img_path["now"] = os.path.join(args.imgdir, "demo_{}.png".format(str(i+1).zfill(num_order)))
    img_path["next"] = os.path.join(args.imgdir, "demo_{}.png".format(str(i+2).zfill(num_order)))

    all_path.append(img_path)

with open("movie_data.json", "w") as f:
    json.dump(all_path, f)
