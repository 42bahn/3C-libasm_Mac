section	.data
	lf db 10
	num db 48
	msg db "A"
	end db "END", 10, 0

section	.text
	global _start

_start :
	mov rax, 1
	mov rdi, 1
	mov rsi, msg
	mov rdx, 1
	mov r10, 1

again :
	cmp r10, 100
	je done
	syscall
	
	mov rax, 1
	inc r10
	jmp again


done :
	mov rax, 60
	mov rdi, 0
	syscall

