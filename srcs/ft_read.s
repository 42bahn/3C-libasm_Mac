section	.text
	global	_ft_read
	extern	___error

_ft_read:
	mov	rax, 2000003
	syscall
	
	jc	set_errno
	
	ret

set_errno:
	push	rax
	
	call	___error

	pop	rbx
	mov	[rax], rbx

	mov	rax, -1
	ret
