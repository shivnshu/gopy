#!/usr/bin/env bash

python3 gen_parser.py $1 > test_parser.py

python test_parser.py

# rm test_parser.py
rm parser.out
rm parsetab.py
