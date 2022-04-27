from setuptools import setup

setup(
    name='CoverallsTesting',
    version='0.0.0',
    packages=['src'],
    url='https://github.com/xingcx/coveralls-testing',
    license='',
    author='Author',
    author_email='',
    description='Testing of Coveralls',
    entry_points={
        'console_scripts': ['test_input_processing=src.test_input_processing:main'],
    }
)
