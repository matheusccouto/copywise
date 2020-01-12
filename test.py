import shutil
import unittest

import copywise


SRC = r'C:\Users\Matheus\Desktop\Google Drive\Code\copywise\Mock Files'
DST = r'C:\Users\Matheus\Desktop\Google Drive\Code\copywise\Copied'


class TestCopyWise(unittest.TestCase):

    def test_ext_is_collection(self):
        arg = 'pdf'
        arg = copywise.assert_is_iter(arg)
        self.assertIsInstance(arg, list)

    def test_find_all_pdf_files(self):
        pdf = copywise.find_files(SRC, 'pdf')
        self.assertEqual(len(pdf), 8)

    def test_find_all_files(self):
        files = copywise.find_files(SRC, None)
        self.assertEqual((len(files)), 8 + 7 + 8)

    def test_find_all_files_except_pdf(self):
        files = copywise.find_files(SRC, include=None, exclude='pdf')
        self.assertEqual(len(files), 7 + 8)
        
    def test_copy_all_pdf_files(self):
        try:
            shutil.rmtree(DST)
        except FileNotFoundError:
            pass
        src = len(copywise.find_files(SRC, 'pdf'))
        copywise.copy_ext(SRC, DST, 'pdf')
        dst = len(copywise.find_files(DST, 'pdf'))
        self.assertAlmostEqual(src, dst)

    def test_copy_pdf_epub_mobi_files(self):
        try:
            shutil.rmtree(DST)
        except FileNotFoundError:
            pass
        src = len(copywise.find_files(SRC, ['pdf', 'epub', 'files']))
        copywise.copy_ext(SRC, DST, ['pdf', 'epub', 'files'])
        dst = len(copywise.find_files(DST, ['pdf', 'epub', 'files']))
        self.assertAlmostEqual(src, dst)

    def test_copy_all_files(self):
        try:
            shutil.rmtree(DST)
        except FileNotFoundError:
            pass
        src = len(copywise.find_files(SRC, None))
        copywise.copy_ext(SRC, DST, None)
        dst = len(copywise.find_files(DST, None))
        self.assertAlmostEqual(src, dst)


if __name__ == '__main__':
    unittest.main()
