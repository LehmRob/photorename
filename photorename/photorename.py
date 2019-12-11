from pathlib import Path
from typing import List
from exif import Image

class Renamer:
	'''Renamer class does the actual analyzing and renaming of the picture files'''
	def __init__(self, directory: str, base_name: str, output_dir: str) -> None:
		self.directory = Path(directory)
		self.base_name = base_name
		self.output_dir = prepare_output_dir(output_dir)

	def __repr__(self) -> str:
		return f"{self.directory.resolve()} --> base name: {self.base_name} in 
			{self.output_dir}"

	def do(self) -> None:
		'''Do is the main entry point for doing the reading and sorting'''
		photos = self.scan_for_photos()

	def scan_for_photos(self) -> List[Path]:
		ret = list()
		for f in self.directory.iterdir():
			if f.is_file():
				ext = f.suffix
				if ext == ".jpg" or ext == ".jpeg" or ext == ".JPG" or ext == ".JPEG"  or ext == ".png":
					photo = Photo(f)
					ret.append(photo)
		return ret

def prepare_output_dir(output_dir: str) -> Path:
	if output_dir == '.':
		# using current output directory
		return Path.cwd()

	p = Path(output_dir)

	if not p.exists():
		p.mkdir()
	elif not p.is_dir():
		raise RuntimeError(f"{output_dir} is no directory")

class Photo():
	def __init__(self, path: Path) -> None:
		with open(path, 'rb') as f:
			self.image = Image(f)
		self.path = path

	def __repr__(self) -> str:
		return f"{self.image}"

	def timestamp(self) -> str:
		return self.image.datetime
