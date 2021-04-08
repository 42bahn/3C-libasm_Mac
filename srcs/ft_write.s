section .text
	global	_ft_write
	extern	___error
_ft_write:
	mov rax, 0x2000004
	syscall
	
	jc	set_errno

	ret

set_errno:
	push    rax

	call    ___error
	
	pop     rbx
	mov     [rax], rbx
	
	mov     rax, -1
	ret
