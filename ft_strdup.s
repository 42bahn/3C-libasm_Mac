section	.texta
	extern	malloc
	extern 	_ft_strlen
	extern	_ft_strcpy
	global	_ft_strdup

_ft_strdup:
	push	rdi
	;mov	rsi, rdi
	
	call	_ft_strlen
	
	inc	rax
	mov	rdi, rax
	call	malloc

	cmp	rax, 0
	je	exit
	
	pop	rsi
	call	_ft_strcpy
	ret

exit:
	ret
