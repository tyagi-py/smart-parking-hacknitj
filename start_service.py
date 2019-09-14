import argparse
import yaml
from coordinates_generator import CoordinatesGenerator
from motion_detector import MotionDetector
from colors import *
import logging


def main():
    logging.basicConfig(level=logging.INFO)

    image_file = "images/new.png"
    data_file = "data/coordinates_1.yml"
    start_frame = 10

    if image_file is not None:
        with open(data_file, "w+") as points:
            generator = CoordinatesGenerator(image_file, points, COLOR_RED)
            generator.generate()

    with open(data_file, "r") as data:
        points = yaml.load(data)
        print(type(points))
        print(points)
        detector = MotionDetector("videos/new.mp4", points, int(start_frame))
        detector.detect_motion()


if __name__ == '__main__':
    main()
