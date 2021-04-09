section	.text
	extern	_malloc
	extern 	_ft_strlen
	extern	_ft_strcpy
	extern	_ft_write
	global	_ft_strdup

_ft_strdup:
	push	rdi
	
	call	_ft_strlen
	
	inc	rax
	mov	rdi, rax
	call	_malloc

	cmp	rax, 0
	je	err_malloc
	
	mov	rdi, rax
	pop	rsi
	call	_ft_strcpy
	ret

err_malloc:
	ret
