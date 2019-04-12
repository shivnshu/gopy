set -e
gcc -m32 -c $1.S -o $1.o
gcc -m32 $1.o -o $1
./$1
rm $1.o
rm $1
