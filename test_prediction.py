import argparse
import time
from typing import Dict, List

import random


def predict(img, ref_position: Dict[str, int] = None):
    return {
        'test': random.randint(0, 10000000),
        'confidence': random.random(),
        'position_top': random.randint(0, 1000),
        'position_right': random.randint(0, 1000),
        'position_bottom': random.randint(0, 1000)+random.randint(0, 1000),
        'position_left': random.randint(0, 1000)+random.randint(0, 1000),
        'time': int(round(time.time() * 1000)) / 1000
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image')
    args = parser.parse_args()
    if args.image:
        print(predict(args.image))


if __name__ == '__main__':
    main()
