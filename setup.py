from setuptools import setup

setup(name='MonteCarlo',
      version='1.0',
      description="Allows the user to play out and analyze Monte Carlo simulations with various amounts of dice of varying faces",
      url='https://github.com/Sonimon123/MonteCarlo',
      author='JR Kargbo',
      license='MIT',
      packages=['MonteCarlo'],
      install_requires = [
        "numpy",
        "pandas",
    ])