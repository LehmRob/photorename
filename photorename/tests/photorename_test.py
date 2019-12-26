from unittest import TestCase
from pathlib import PurePath, Path
from tempfile import mkdtemp
from shutil import rmtree
from hashlib import sha256

import photorename

def hash_for_file(filepath: Path) -> str:
    with open(filepath, 'rb') as f:
        cnt = f.read()
        hash = sha256(cnt)
        return hash.hexdigest()

class TestRenamer(TestCase):
    def test_do(self):
        expected_order = [
            'ee7e84526b423ad8f22269d3b1936d2f85cd7faa6f6944b86c68ffe31e31bac7',
            '55a5d7a1cebc0ead7333b68bd12c35fbf230ce400ecfa9ba58d63e590dfd6df0',
            '9ad51101a85ade792971e0f23f36092e4d1d929f561ed02416b1251abf2fbf64',
        ]

        output = mkdtemp()
        testdir = PurePath.joinpath(Path.cwd(), "test_photos")
        print(f"Testdir {testdir} Output {output}")
        r = photorename.Renamer(testdir, "test", output)
        r.do()
        output_dir = Path(output)

        files = list()
        for f in output_dir.iterdir():
            files.append(f)

        files.sort()
        self.assertTrue(len(files) == 3)
        print(f"Hash for file {hash_for_file(files[0])}")
        self.assertTrue(hash_for_file(files[0]) == expected_order[0]) 
        print(f"Hash for file {hash_for_file(files[1])}")
        self.assertTrue(hash_for_file(files[1]) == expected_order[1]) 
        print(f"Hash for file {hash_for_file(files[2])}")
        self.assertTrue(hash_for_file(files[2]) == expected_order[2]) 

        rmtree(output)
