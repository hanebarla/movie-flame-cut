import os
import argparse
import cv2


def movie_cut(movie_path):
    cap = cv2.VideoCapture(movie_path)

    if not cap.isOpened():
        return

    ex_place = movie_path.rfind('.')
    dir_path = movie_path[:ex_place]
    print(dir_path)

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, "demo")

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), 'png'), frame)
            n += 1
        else:
            return


if __name__ == "__main__":
    absdirpath = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser()
    parser.add_argument("--moviedir", default=absdirpath)
    args = parser.parse_args()

    files = os.listdir(args.moviedir)
    movie_pathlist = [os.path.join(args.moviedir, f) for f in files if os.path.isfile(os.path.join(args.moviedir, f))]

    for p in movie_pathlist:
        movie_cut(p)

    print("Done")
