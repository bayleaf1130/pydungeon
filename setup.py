import setuptools

with open('AUTHORS', 'r') as file:
    authors = file.read().strip()

with open('README.md', 'r') as file:
    long_description = file.read().strip()

with open('VERSION', 'r') as file:
    version = file.read()

setuptools.setup(
    name='pydungeon', # The name
    author=authors,
    version=version,
    description='Python D & D Library',
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': ['dungeon=pydungeon:__main__']
    }
)
