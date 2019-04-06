import random
from time import sleep


def test(i, j, k, image):
    sleep(0.5)
    accuracy = random.random()
    print("i:{}, j:{}, k:{}, image:{}, accuracy: {}".format(i, j, k, image, accuracy))
    return accuracy


def train(i, j, k, images):
    # sleep(100)
    accuracy = random.random()
    print("i:{}, j:{}, k:{}, images:{}, accuracy: {}".format(i, j, k, images, accuracy))
    return accuracy
