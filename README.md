# Projector
Automate your projects

# Requirements
* python 3.6
* cygwin for Windows

# Usage
* create project path (or use old)
* run inside folder 

```bash
projector build
```
* Modify PROJECTFILE
for example
```makefile
run:
  # open path if project starts
  .
  # open some programs
  subl
  pycharm
  # open links with chrome
  https://github.com/sokolegg/Projector
close:
  # windows to close after work (with projector stop)
  all
metrics:
  keyboard
  codecount github.com/sokolegg/Projector
  ...
'''
