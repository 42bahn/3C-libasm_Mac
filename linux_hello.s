section	.data;	초기값이 있는 전역 변수/정적 변수를 선언하는 공간
	msg db "hello world", 0x0A

section	.text; 실행할 코드를 작성하는 공간
	global _start

_start :
	mov rax, 1; syscall write()
	; rax : 산술/논리 연산을 수행하며 함수의 return 값이 저장된다.
	; 시스템콜 함수를 사용하려면 rax에 함수의 syscall 번호를 넣어준다.
	mov rdi, 1; write() 첫 번째 매개변수
	; rdi : 데이터가 복사된 dest 데이터의 주소가 저장된다.
	mov rsi, msg; write() 두 번째 매개변수
	; rsi : 데이터를 복사할 src 데이터의 주소가 저장된다.
	mov rdx, 12; write() 세 번째 매개변수
	syscall
	mov rax, 60; syscall exit()
	mov rdi, 0 ; exit() 매개변수
	syscall

; compile : nsam -f elf64 linux_hello.s
; create execute file : ld hello.o -o hello 		
