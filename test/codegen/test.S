.section .text
.globl _main

_main:
call _init
call main
push $0
call exit

_init:
push %ebp
movl %esp, %ebp
movl %ebp, %esp
pop %ebp
ret

main:
movl $10, -4(%ebp)
negl -4(%ebp)
movl $20, -8(%ebp)
