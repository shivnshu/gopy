set -e
gcc -m32 -c $1.S -o $1.o 2> /dev/null
gcc -m32 $1.o -o $1 2> /dev/null
rm $1.S
rm $1.o
# gcc -m32 -Llib -lprint $1.o -o $1.out > /dev/null
# LD_LIBRARY_PATH=lib ./$1.out
# rm $1.o
#rm $1.out
# echo ""
# echo "*Executed successfully*"
