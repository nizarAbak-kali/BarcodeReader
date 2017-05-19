#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zbar
import zbar.misc


def get_barcode():
    print "reading ...."

    scanner = zbar.ImageScanner()
    image = read_image_into_numpy_array(...) # get an image into a numpy array
    scanner = zbar.Scanner()
    results = scanner.scan(image)

    for result in results:
        if result.type == 'UPC-A':
            print(result.data, zbar.misc.upca_is_valid(result.data.decode('ascii')))



if __name__ == '__main__':
    get_barcode()