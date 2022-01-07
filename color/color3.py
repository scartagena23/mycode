#!/usr/bin/env python3

import crayons

def main(first:str, second:str):
    print(crayons.yellow(first) + crayons.blue(second))

if __name__ == '__main__':
    main("shei","la")
    
