#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys

class a():
    def __init__(self,
                 item,
                 price):
        self.item  = str(item).strip()
        self.price = price
    def __str__(self):
        return ('{} = {}'.format(
            self.item,
            self.price,
        ))


class b(a):
    def __init__(self,
                 item,
                 price,
                 desc):
        a.__init__(self, item, price)
        self.desc  = str(desc).strip()


def main():
    x=a('A1500', 2.50)
    print(x)
    # A1500 = 2.5

    y=b('B2700', 3.5, 'Water soluble')
    print(y)
    # this runs class a's __str__.
    # B2700 = 3.5


if __name__=='__main__':

    # logger setup
    logfile = str(sys.argv[0])[:-3] + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    main()
