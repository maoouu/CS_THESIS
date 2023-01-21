import sys
sys.path.append('../')

import unittest
from utils.file_handling import file_is_allowed


class TestFileIsAllowed(unittest.TestCase):
    def test_mp3(self):
        sample_name = 'abc.mp3'
        self.assertTrue(file_is_allowed(sample_name))
    

    def test_wav(self):
        sample_name = 'abc.wav'
        self.assertTrue(file_is_allowed(sample_name))

    
    def test_mp3_multiple_extensions(self):
        sample_name = 'abc.ttf.gif.mp3'
        self.assertTrue(file_is_allowed(sample_name))


    def test_wav_multiple_extensions(self):
        sample_name = 'abc.mp4.gif.ttf.wav'
        self.assertTrue(file_is_allowed(sample_name))
    

    def test_wrong_extension(self):
        sample_name = 'abc.gif'
        self.assertFalse(file_is_allowed(sample_name))


    def test_multiple_dots_wrong_extension(self):
        sample_name = 'abc.def.ghi.docx.mp4'
        self.assertFalse(file_is_allowed(sample_name))

    
    def test_no_extensions(self):
        sample_name = 'abcdefghijkl'
        self.assertFalse(file_is_allowed(sample_name))


    def test_all_dots(self):
        sample_name = '.............'
        self.assertFalse(file_is_allowed(sample_name))



if __name__ == '__main__':
    unittest.main()