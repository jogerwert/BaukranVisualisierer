from distutils.core import setup
import py2exe

setup(
    name='BaukranVisualisierer',
    version='0.1',
    console=['baukran_visualisierer.py'],
    install_requires=[
          'vpython',
    ]
)
