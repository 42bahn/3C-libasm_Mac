section .text
	global _ft_strcmp

_ft_strcmp:
	mov	rax, 0
	mov	rbx, 0
	mov 	rcx, 0
	jmp	check

check:
	mov	al, BYTE [rdi + rcx]
	mov	bl, BYTE [rsi + rcx]

	cmp	al, 0x00
	je	end

	cmp	al, bl
	jne	end

	inc	rcx
	jmp	check

end:
	sub	rax, rbx
	ret

