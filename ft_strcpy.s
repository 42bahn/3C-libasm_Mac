section	.text
	global _ft_strcpy

_ft_strcpy:
	mov	rcx, 0
	jmp	check
	
check:
	cmp	BYTE [rsi + rcx], 0x00
	jne	copy
	mov	BYTE [rdi + rcx], 0x00
	mov	rax, rdi
	ret

copy:
	mov	al, BYTE [rsi + rcx]
	mov	BYTE [rdi + rcx], al
	inc	rcx
	jmp	check

