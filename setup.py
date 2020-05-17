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
    },
    install_requires=['docutils; platform_system == "Windows"',
                      'pygments; platform_system == "Windows"',
                      'pypiwin32; platform_system == "Windows"',
                      'kivy_deps.sdl2==0.1.*; platform_system == "Windows"',
                      'kivy_deps.glew==0.1.*; platform_system == "Windows"',
                      'kivy_deps.gstreamer==0.1.*; platform_system == "Windows"',
                      'kivy==1.11.1; platform_system == "Windows"',
                      'pyYAML;',
                      'pytest;']
)
