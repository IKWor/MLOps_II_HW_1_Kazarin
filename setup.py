from setuptools import setup, find_packages

setup(
    name='credit_default_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'perform_eda=eda:perform_eda',
        ],
    },
)
