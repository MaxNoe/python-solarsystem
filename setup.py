from setuptools import setup, find_packages

setup(
    name='solarsystem',
    version='0.0.1',
    description='Simulate solar systems',
    url='http://github.com/MaxNoe/python-solarsystem',
    author='Maximilian Noethe',
    author_email='maximilian.noethe@tu-dortmund.de',
    license='MIT',
    packages=find_packages(),
    tests_require=['pytest>=3.0.0'],
    setup_requires=['pytest-runner'],
    install_requires=[
        'numpy',
        'scipy',
    ],
    zip_safe=False,
)
