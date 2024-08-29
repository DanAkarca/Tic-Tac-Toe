from setuptools import setup, find_packages

setup(
    name="tic-tac-toe",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'tic-tac-toe=main:play_game',
        ],
    },
    author="Danyal Akarca",
    author_email="danyal.akarca@gmail.com",
    description="A simple Tic-Tac-Toe game",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DanAkarca/tic-tac-toe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)