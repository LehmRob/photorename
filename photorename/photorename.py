from pathlib import Path, PurePath
from typing import List
from exif import Image
from shutil import copy2

class Photo():
    def __init__(self, path: Path, suffix: str) -> None:
        with open(path, 'rb') as f:
                self.image = Image(f)
        self.path = path
        self.suffix = suffix

    def __repr__(self) -> str:
        return f"{self.path}"

    def timestamp(self) -> str:
        return self.image.datetime

    def path(self) -> Path:
        return self.path

class Renamer:
    '''Renamer class does the actual analyzing and renaming of the picture files'''
    def __init__(self, directory: str, base_name: str, output_dir: str) -> None:
        self.directory = Path(directory).expanduser()
        self.base_name = base_name
        self.output_dir = prepare_output_dir(output_dir)

    def __repr__(self) -> str:
        return f"{self.directory.resolve()} --> base name: {self.base_name} in {self.output_dir}"

    def do(self) -> None:
        '''Do is the main entry point for doing the reading and sorting'''
        photos = self.scan_for_photos()
        sorted_photos = sorted(photos, key=lambda photo: photo.timestamp())
        self.copy_photos(sorted_photos)

    def scan_for_photos(self) -> List[Photo]:
        ret = list()
        for f in self.directory.iterdir():
            if f.is_file():
                ext = f.suffix
                if ext == ".jpg" or ext == ".jpeg" or ext == ".JPG" or ext == ".JPEG"  or ext == ".png":
                    photo = Photo(f, ext)
                    ret.append(photo)
        return ret

    def copy_photos(self, sorted_photos: List[Photo]) -> None:
        counter = 1
        for photo in sorted_photos:
            file_name = PurePath(f"{self.base_name}_{counter:04}.{photo.suffix}")
            target_path = PurePath.joinpath(self.output_dir, file_name)
            copy2(photo.path, target_path)
            counter += 1


def prepare_output_dir(output_dir: str) -> Path:
    p = Path(output_dir)
    if output_dir == '.':
        # using current output directory
        return Path.cwd()
    elif output_dir.find('~'):
        p = Path(output_dir).expanduser()

    if not p.exists():
        p.expanduser().mkdir()
    elif not p.is_dir():
        raise RuntimeError(f"{output_dir} is no directory")

    return p

