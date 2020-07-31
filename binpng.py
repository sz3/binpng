import sys
from math import sqrt

from PIL import Image

from palette import palette


def _get_best_dimensions(n):
    small_divisors = [d for d in range(2, int(sqrt(n))) if n % d == 0]
    if not small_divisors:
        return (n, 1)

    # divisors[-1] is the largest divisor below sqrt(n)
    # we'll use it as the height, and the bigger number as the width
    height = small_divisors[-1]
    return (n // height, height)


def decode(src_file, dst_file):
    img = Image.open(src_file)
    with open(dst_file, 'wb') as f:
        for p in img.getdata():
            bites = bytearray((p,))
            f.write(bites)


def encode(src_file, dst_file):
    with open(src_file, 'rb') as f:
        contents = f.read()

    # I think we need to encode the length + maybe pad.
    # or at least, add an option. Feels bad!
    pixels = len(contents)
    imgSize = _get_best_dimensions(pixels)
    img = Image.frombytes('P', imgSize, contents, 'raw')
    img.putpalette(palette())
    img.save(dst_file)


def main():
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    if src_file.endswith('.png'):
        decode(src_file, dst_file)
    else:
        encode(src_file, dst_file)


if __name__ == '__main__':
    main()
