from unittest import TestCase
from pathlib import PurePath, Path
from tempfile import mkdtemp
from shutil import rmtree

import photorename

class TestRenamer(TestCase):
    def test_do(self):
        output = mkdtemp()
        testdir = PurePath.joinpath(Path.cwd(), "test_photos")
        print(f"Testdir {testdir} Output {output}")
        r = photorename.Renamer(testdir, "test", output)
        r.do()

        self.assertTrue(1==1)

        rmtree(output)
