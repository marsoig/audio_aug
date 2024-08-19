import unittest
from unittest.mock import patch, call
import random
import ffmpegio

from audioaugment import augment

class TestAugmentAudioFFMPEGIO(unittest.TestCase):

    @patch('ffmpegio.transcode')
    @patch('random.uniform')
    @patch('random.random')
    def test_augment_audio_ffmpegio_with_highpass(self, mock_random, mock_uniform, mock_transcode):
        # Set up mock values for uniform and random
        mock_uniform.side_effect = [0.1, 0.8, 200.0]  # Pitch shift factor, atempo, volume, highpass frequency
        mock_random.return_value = 0.6  # Random highpass filter is applied
        
        pitch_shift_factor = 2**0.1
        
        input_file = 'input.wav'
        output_file = 'output.wav'
        
        augment.augment_audio_ffmpegio(input_file, output_file)
        
        expected_filters = f'asetrate=44100*{pitch_shift_factor},atempo={1/pitch_shift_factor},volume=0.8,highpass=f=200.0'

        mock_transcode.assert_called_once_with(
            input_file,
            output_file,
            acodec='pcm_s16le',
            af=expected_filters
        )

    @patch('ffmpegio.transcode')
    @patch('random.uniform')
    @patch('random.random')
    def test_augment_audio_ffmpegio_without_highpass(self, mock_random, mock_uniform, mock_transcode):
        # Set up mock values for uniform and random
        mock_uniform.side_effect = [0.2, 1.1]  # Pitch shift factor, volume
        mock_random.return_value = 0.4  # Random highpass filter is NOT applied
        
        pitch_shift_factor = 2**0.2
        
        input_file = 'input.wav'
        output_file = 'output.wav'
        
        augment.augment_audio_ffmpegio(input_file, output_file)
        
        expected_filters = f'asetrate=44100*{pitch_shift_factor},atempo={1/pitch_shift_factor},volume=1.1'

        mock_transcode.assert_called_once_with(
            input_file,
            output_file,
            acodec='pcm_s16le',
            af=expected_filters
        )

if __name__ == '__main__':
    unittest.main()
