from pathlib import Path
from exif import Image

class Photo():
	def __init__(self, path: Path) -> None:
		with open(path, 'rb') as f:
			self.image = Image(f)
		self.path = path

	def __repr__(self) -> str:
		return f"{self.image}"

	def timestamp(self) 
