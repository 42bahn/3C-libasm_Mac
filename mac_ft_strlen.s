section .text
	global _ft_strlen

_ft_strlen:
	mov rax, 0
	jmp _count
_count:
	cmp BYTE [rdi + rax], 0x00
	je _end	

	inc rax
	jmp _count	

_end:
	ret

