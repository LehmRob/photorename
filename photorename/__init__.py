import argparse
from pathlib import Path
from .photorename import Renamer


def run():
    parser = argparse.ArgumentParser(
        description='Bulk rename pictures in a directory')
    parser.add_argument('directory', metavar='dir', 
        help='directory with the fotos which should be ordered')
    parser.add_argument('-n', '--name', dest='name', default='pic', 
        help='base name for pictures; the filename is extended with a number (e.g. pic-001.png)')
    parser.add_argument('-o', '--output', dest='output', default='.',
        help="""output directory for the sorted pictures, if not used default is the current 
        directory""")

    args = parser.parse_args()

    renamer = Renamer(args.directory, args.name, args.output)
    print(renamer)
    renamer.do()

