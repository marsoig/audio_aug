from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Applies random augmentation to audio files'
LONG_DESCRIPTION = 'Applies random augmentation to one audio file of any type'

# Setting up
setup(
        name="audioaugment", 
        version=VERSION,
        author="Maria Sokolova",
        author_email="maria.i.sokolova.2000@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['ffmpegio', 'scipy', 'numpy'],
        entry_points = {
            'console_scripts': ['audio_augment=audioaugment.augment:main', 'audio_augment_test=audioaugment.test.run_tests:run_all_tests'],
        },
        
        keywords=['audio', 'augmentation'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)