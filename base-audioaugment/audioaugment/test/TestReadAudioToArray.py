import unittest
from unittest.mock import patch, mock_open
import os
import tempfile
import ffmpegio
import scipy.io.wavfile as wav

# Assume the read_audio_to_array function is defined in a module called audio_module
from audioaugment import augment

class TestReadAudioToArray(unittest.TestCase):

    @patch('scipy.io.wavfile.read')  # Mock wav.read for successful .wav file read
    def test_read_audio_wav_file(self, mock_wav_read):
        # Set up the mock to return a sample rate and data
        mock_wav_read.return_value = (44100, [1, 2, 3, 4])

        file_path = 'test.wav'

        samplerate, data = augment.read_audio_to_array(file_path)

        mock_wav_read.assert_called_once_with(file_path)

        self.assertEqual(samplerate, 44100)
        self.assertEqual(data, [1, 2, 3, 4])

    @patch('os.remove')  # Mock os.remove to avoid actual file removal
    @patch('tempfile.mktemp')
    @patch('ffmpegio.transcode')
    @patch('scipy.io.wavfile.read')
    def test_read_audio_non_wav_file(self, mock_wav_read, mock_transcode, mock_mktemp, mock_remove):
        # Mock wav.read to raise ValueError when first called, simulating a non-wav file
        mock_wav_read.side_effect = [ValueError, (44100, [1, 2, 3, 4])]

        mock_mktemp.return_value = 'temp_file.wav'

        file_path = 'test.mp3'

        samplerate, data = augment.read_audio_to_array(file_path)

        mock_transcode.assert_called_once_with(file_path, 'temp_file.wav')

        mock_wav_read.assert_called_with('temp_file.wav')

        mock_remove.assert_called_once_with('temp_file.wav')

        self.assertEqual(samplerate, 44100)
        self.assertEqual(data, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
