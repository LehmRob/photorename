import argparse
from pathlib import Path
from typing import List
from .photo import Photo


def run():
	parser = argparse.ArgumentParser(
		description='Bulk rename pictures in a directory')
	parser.add_argument('directory', metavar='dir', help='directory with the fotos which should be ordered')
	parser.add_argument('-n', '--name', dest='name', default='pic', 
		help='base name for pictures; the filename is extended with a number (e.g. pic-001.png)')
	parser.add_argument('-o', '--output', dest='output', default='.',
		help='output directory for the sorted pictures, if not used default is the current directory')

	args = parser.parse_args()

	renamer = Renamer(args.directory, args.name, args.output)
	print(renamer)
	renamer.do()

def prepare_output_dir(output_dir: str) -> Path:
	if output_dir == '.':
		# using current output directory
		return Path.cwd()

	p = Path(output_dir)

	if not p.exists():
		p.mkdir()
	elif not p.is_dir():
		raise RuntimeError(f"{output_dir} is no directory")


class Renamer:
	'''Renamer class does the actual analyzing and renaming of the picture files'''
	def __init__(self, directory: str, base_name: str, output_dir: str) -> None:
		self.directory = Path(directory)
		self.base_name = base_name
		self.output_dir = prepare_output_dir(output_dir)

	def __repr__(self) -> str:
		return f"{self.directory.resolve()} --> base name: {self.base_name} in {self.output_dir}"

	def do(self) -> None:
		photos = self.scan_for_photos()
		sorted_photos = sort(photos, lambda photos: )

	def scan_for_photos(self) -> List[Path]:
		ret = list()
		for f in self.directory.iterdir():
			if f.is_file():
				ext = f.suffix
				if ext == ".jpg" or ext == ".jpeg" or ext == ".JPG" or ext == ".JPEG"  or ext == ".png":
					photo = Photo(f)
					ret.append(photo)
		return ret
