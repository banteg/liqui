from setuptools import setup

setup(
    name='liqui',
    version='1.0.0',
    description='liqui.io api wrapper',
    long_description=open('readme.md', 'rt').read(),
    url='https://github.com/banteg/liqui',
    author='banteg',
    license='MIT',
    py_modules=['liqui'],
    install_requires=['requests']
)
