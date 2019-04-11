#!/usr/bin/env bash
set -e
nasm -f elf64 -o $1.o $1.asm
ld  -o $1 $1.o
rm $1.o
./$1
rm $1
