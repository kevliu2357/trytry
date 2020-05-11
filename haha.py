import sys

print(sys.version)
print(sys.executable)


a = 1


while a < 10:
    if a <= 5:
        print(a)
    else:
        print("hello")
    a = a + 1
else:
    print("test")


## Choose python interpreter

## Create virtual environment:       python3 -m venv myvenv

## Choose 'python interpreter' in 'new created virtual enviroment'

## Kill the terminal;      Restart the terminal

## Install black & pylint (if those does not work):      pip install -U pylint ;  pip install -U black

## Interactive python:
# name = input("Your Name? ")
# print("Hello,", name)
# run above two lines with  " run in the terminal"

## Command pallet:  cmd + shift + p

## Show terminal:   ctrl + ~

## Clear terminal:  cmd + k

## Check 'current working directory':    pwd (in terminal)

## Auto formatting:  option + shift + f

## In command pallet :  sort imports

## Run current python file;      ctrl + option + N


## In User Settings (Jason version):  ctrl + space  (type 'editor' will show all 'editor' related setting options)

# {
#     "workbench.colorTheme": "Predawn",
#     "workbench.iconTheme": "ayu",
#     "workbench.settings.editor": "json",
#     "workbench.settings.openDefaultSettings": true,
#     "workbench.settings.useSplitJSON": true,
#     "python.pythonPath": "/Library/Frameworks/Python.framework/Versions/3.7/bin/python3",
#     "python.formatting.provider": "black",
#     "editor.formatOnSave": true,
#     "python.linting.enabled": true,
#     "code-runner.executorMap": {
#         "python": " $pythonPath -u $fullFileName "
#     },
#     "code-runner.showExecutionMessage": true,
#     "code-runner.clearPreviousOutput": false,
#     "python.dataScience.sendSelectionToInteractiveWindow": true
# }

## 首次 使用 git
# Create script ".gitignore" ---- 文件的内容输入: '你的虚拟环境的名字' (第一行)； '.vscode' (你的个人的一些设定) ---- 保存文件 ----
# Click "Initiate Repository" ---- click "+"(Stages Changes) ---- click "v(对号)" (Commit) ---- input commit message ----
# in terminal: git remote add origin https://github.com/kevliu2357/你在github上创建的repository的名字.git （可以在github页面的” push an existing repository from the command line“ 找到）----
# Click "..." ---- Select "push to"


## 非首次 使用 git 来 track changes
# Click "+"(Stages Changes) ---- click "v(对号)" (Commit) ---- input commit message ----
# Click "..." ---- Select "push to"

## for demonstrating debugging
