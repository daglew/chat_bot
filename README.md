# chat_bot
This is a file describing how to prepare the environment for creating a chatbot application.
## Table of contents
* [Clone repository](#clone-repository-using-git-bash)
* [Installation virtual environment](#installation-virtual-environment-venv)
* [Create a new branch](#create-a-new-branch)



## Clone repository using Git Bash

1. Clone repository to your local machine use command.
``` 
git clone https://github.com/daglew/chat_bot.git
cd .venv
``` 
## Installation virtual environment (venv)

```
1. CreatE a virtual environment called venv in the current path
Create venv 
python3 -m pip install virtualenv
python3 -m venv ./venv

2. Command that activates the virtual environment
Activate venv
source venv/Scripts/activate

3. Command to install packages
pip install -r chat_bot/.venv

4. set up interpreter
PyCharm -> File -> Settings -> Python interpreter ->zębatka -> Add -> Existing environment -> ...  -> Interpreter -> <path>/venv/Scripts/python f.e path
``` 
## Create a new branch

```
1. Open Pycharm
2. Go to terminal
3. Use command "git status"
4. Check on what branch are you ( there should be information that you are on develop branch)
5. Create a new branch use command "git checkout -b chatbot_first_commit"
6. Use command "git status"
7. Check on what branch are you
8. Use command "git checkout develop"
9. Check on what branch are you
10. Use command "git checkout chatbot_first_commit"
11. Check on what branch are you
12. Go to develop branch
13. Delete the branch "git branch -d <chatbot_first_commit>

```

```bash
#!/bin/bash
#installing the virtualenv package
echo 'Execute command: python3 -m pip install virtualenv, Installing virtualenv package'
python3 -m pip install virtualenv

#installation of the virtual environment to the chatbot_first_commit file (I can change and substitute this,
#will be created in the file where we enforce it
echo "Execute command: python3 -m virtualenv chatbot_first_commit, installing environament into the virtual_environment folder"
python3 -m virtualenv chatbot_first_commit

#environmental activation
echo 'Execute command: source virtual_environment/Scripts/activate, ACTIVATE PYTHON'
source virtual_environment/Scripts/activate

#install external packages from the location where we call requirements.txt (must be in the same path)
echo "Execute command: pip install -r requirements.txt, installing all aditional packages"
pip install -r requirements.txt 
```
