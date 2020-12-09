PYTHON

usage: proc_log.py [-h] [-o OUTPUT] [-j] input

Process log file from nginx.

positional arguments:
  input                 Path for log file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path for results. Default: res.txt
  -j, --json            Choose to save as json format
  
BASH

usage: ./proc_log.sh access.log
Результат запишется в файл res.