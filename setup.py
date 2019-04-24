from setuptools import setup, find_packages

setup(
    name='Sapiri',
    version='0.0.1',
    url='https://github.com/mypackage.git',
    author='Antonio Lima',
    author_email='anto87@gmail.com',
    description='A wiki',
    packages=find_packages(),    
    entry_points={
        'console_scripts': [
            'sapiri = sapiri.serve:main'
        ]
    },
)
