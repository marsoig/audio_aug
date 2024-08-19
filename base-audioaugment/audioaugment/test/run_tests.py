import unittest

from audioaugment.test import TestAugmentAudioFFMPEGIO
from audioaugment.test import TestReadAudioToArray

def run_all_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestAugmentAudioFFMPEGIO.TestAugmentAudioFFMPEGIO))
    suite.addTests(loader.loadTestsFromTestCase(TestReadAudioToArray.TestReadAudioToArray))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    run_all_tests()
