.section .text
.globl main

main:
call _init
call func_main
push $0
call exit

_init:
push %ebp
movl %esp, %ebp
movl %ebp, %esp
pop %ebp
ret

func_main:
push %ebp
mov %esp, %ebp
movl $10, -4(%ebp)
negl -4(%ebp)
push $string_0
call printf
mov %ebp, %esp
pop %ebp
ret

.section .data
string_0: .string "abcd\n"