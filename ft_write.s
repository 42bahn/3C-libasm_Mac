section .text
	global	_ft_write

_ft_write:
	mov rax, 1
;	mov rax, 0x2000004	MacOS
	
	syscall
	ret
