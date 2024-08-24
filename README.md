## A test task for a Data Scientist job

1. Write a processor (function/class) that augments audio data.
The number of augmentations is up to you.

Augmentations can significantly change the audio signal, but serious degradation of the final data should be avoided. The augmentation result should still be similar to human speech.

This processor receives a numpy array with an audio signal as input, shape=(num_channels, num_samples), dtype=float32, order=“F”. Both mono (num_channels == 1) and stereo (num_channels == 2) signals should be supported.

The output is a similar (same dtype, order and num_channels, but num_samples may differ) signal in the form of a numpy array.

2. Write a CLI application that
1). takes the path to an audio file as input
2). reads it into a numpy array
3). augments it using the processor from step 1
4). saves the result into an audio file.
   
Additional conditions and restrictions

- You can use any modules of the standard Python library, as well as external packages: numpy, scipy, numba, Cython, ffmpegio. Using other external packages (such as librosa, audiomentations, etc.) is not allowed.
- You can and do use external applications for working with audio via Linux pipes using the subprocess module.
- You can have unit tests, as well as make your application a full-fledged Python package.

### Usage:
To install, in base_audioaugmentation run:
`pip install .`

To run on file, do:
`audio_augment filename`

To test, do:
`audio_augment_test`
