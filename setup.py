from setuptools import setup, find_packages
setup(
    name="tictactoe-yourusername",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'tictactoe=tictactoe.main:play_game',
        ],
    },
    author="Danyal Akarca",
    author_email="danyal.akarca@gmail.com",
    description="A simple Tic-Tac-Toe game",
    long_description="This package provides a command-line implementation of the classic Tic-Tac-Toe game.",
    long_description_content_type="text/markdown",
    url="https://github.com/DanAkarca/tictactoe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='3.7.4',
)