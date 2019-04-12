set -e
gcc -m32 -c $1.S
gcc -m32 $1.o
./$1
rm $1.o
rm $1
