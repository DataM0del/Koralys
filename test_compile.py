import unittest
from compile.compile import download_compiler

class TestCompiler(unittest.TestCase):
    """Tests the compiler script."""

    def test_downloader(self):
        download_compiler()

if __name__ == '__main__':
    unittest.main()
