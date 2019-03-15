from setuptools import setup

requirements = ['click']

setup(
    name='vanellope',
    version='0.0.1',
    license='MIT',
    packages=['vanellope'],
    zip_safe=False,
    install_requires=requirements,
    entry_points={'console_scripts': ['vanellope = vanellope:cli']},
)
