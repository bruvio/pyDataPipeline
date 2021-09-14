from setuptools import setup, find_packages

setup(
    name='data-pipeline-api',
    version='0.1',
    author='SCRC / FAIR',
    description='Python FAIR data pipeline API (DPAPI)',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyYAML==5.3.1',
        'requests==2.23.0',
        'scipy',
        'h5py>=3.4.0'
        ]
)
