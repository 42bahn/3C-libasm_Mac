section	.data
	msg	db	"abcde", 0x0a, 0x00
section .text
	global _start

_start:
	mov rcx, 0
	mov rdi, msg
	call _ft_strlen
	
	add rcx, 48

	mov rax, 1
	
	mov rdi, 1
	mov rsi, rcx
	mov rdx, 1	
	syscall

	mov rax, 60
	mov rdi, 0
	syscall

_ft_strlen:
	cmp BYTE [rdi + rcx], 0x00
	je _end	

	inc rcx
	jmp _ft_strlen	

_end:
	ret

