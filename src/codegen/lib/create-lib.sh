#!/usr/bin/env bash
set -e
gcc -m32 -c float_print.c -o float_print.o
gcc -m32 -shared -o libprint.so float_print.o
