# Text Obfuscator
A command-line tool written in Python 3 that makes a text unintelligible but readable

## Installation
#### Create Virtual Environment for Python 3
- Install Python 3
``
sudo apt install Python3
``
- Install Python Virtual Environment
``
sudo apt install python3-venv
``
- Clone project
``
git clone https://github.com/benjaminAyangbola/text-obfuscator.git
``
- Activate the Text Obfuscator virtual environment to start using it
``
source path/to/text-obfuscator/bin/activate
``

#### Install packages
- Install Click: a Python package for creating beautiful command line interfaces
``
pip3 install click
``
- Install pyfiglet
``
pip3 install pyfiglet
``

#### For command options
``
python3 index.py --help
``
#### Run
Use the command below to see how Text Obfuscator works:
``
python3 index.py --text="Mary had a little lamb"
``