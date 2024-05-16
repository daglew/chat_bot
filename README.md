## Chat_bot
This is a file describing how to prepare the environment for creating a chatbot application.
## Table of contents
* [Clone repository](#clone-repository-using-git-bash)
* [Installation virtual environment](#installation-virtual-environment-venv)



## Clone repository using Git Bash

1. Clone repository to your local machine use command.
``` 
git clone https://github.com/daglew/chat_bot.git
``` 

2. Go to the chatbot folder with the given command.
``` 
cd chat_bot/
``` 
## Installation virtual environment

3. Installing the virtualenv package
'Execute command: python3 -m pip install virtualenv, Installing virtualenv package'.
```
python3 -m pip install virtualenv
```

4. Installation of the virtual environment to the .venv file (I can change and substitute this,
will be created in the file where we enforce it
"Execute command: python3 -m virtualenv .venv, installing environament into folder".
```
python3 -m virtualenv .venv
```
5. Environmental activation
'Execute command: source virtual_environment/Scripts/activate, ACTIVATE PYTHON'
```
source .venv/Scripts/activate
```
6. Install external packages from the location where we call requirements.txt (must be in the same path)
"Execute command: pip install -r requirements.txt, installing all aditional packages"
```
pip install -r requirements.txt 
```
7. Execute the given command to open the project.
```
python3 main.py
```
