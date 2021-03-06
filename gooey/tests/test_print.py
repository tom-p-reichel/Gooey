import sys

from gooey import Gooey
from gooey import GooeyParser
from argparse import ArgumentParser

@Gooey(
    menu=[{
        "name": "File",
        "items": [{
                  "type":"PrintDialog",
                  "menuTitle":"Printy",
                  "font":"SCRIPT",
                  "size":30
                 }]
        }]
)
def main():
    desc = "Example application to show Gooey's various widgets"
    parser = GooeyParser(prog="example_print")
    _ = parser.parse_args(sys.argv[1:])

    print('Hello, world!\nNewlines work fine!')

if __name__ == '__main__':
    main()

