section	.data
	LF	db	0x0a;	EMPTY 변수에 '\n'를 저장
	STAR	db	'*';	STAR 변수에 '*' 문자를 저장

section	.text
	global	_start

_start:
	mov	rax, 1
	mov	rdi, 1
	mov	rdx, 1
	;	syscall write 함수 설정
	
	mov	r10, 0 ;	r10 레지스터를 인덱스 변수로서 사용
	mov	r9, [rsp + 16]
	;	rsp 스택 포인터 레지스터를 통해
	;	입력 값(문자열)이 저장된 위치의 값을 
	;	r9 레지스터에 저장
	;		* 대괄호는 해당 주소가 가리키는 값을 의미한다.
	cmp r9, 0	;	r9(입력 값)가 0일 경우 또는 입력 값이 없을 경우
	je _done	;	_done 함수로 JUMP

	mov	cl, [r9];	cl(RCX의 하위 8bit) : r9의 1 byte 값(0 ~ 9)을 cl에 저장 
	movzx	r9, cl	;	문자 형태의 cl 값을 r9에 저장
	sub	r9, 0x30;	r9 - 48. 아스키 코드 문자 값을 숫자 값으로 변환하여 저장 

	mov	r8, r9	;	r8 레지스터에 r9 값을 저장한다.
	xor	r9, r9	;	r9 레지스터를 0으로 초기화
	call	_syscall
	;	call 명령을 통해 다음 명령줄의 주소 값을 스택(EIP)에 저장한다.
	;	_syscall 함수 호출

_small:
	cmp	r10, r9 
	je	_up
	;	초기에 r10, r9의 값이 모두 0 이기 때문에 _up 함수로 JUMP하게된다.
	;	하지만 이전에 _syscall 함수를 호출하면서 
	;	rax에 리턴 값이 저장되어진 상태이기 때문에
	;	_up 함수에서 syscall 하여도 write 함수를 통해 개행문자는 출력되지 않게된다.
	mov	rsi, STAR;	write 출력 문자 = '*' 설정
	syscall		;	write 함수 호출
	
	mov	rax, 1	;	write 함수 설정		
	inc	r10	;	r10 1 증가
	
	jmp	_small	;	small 함수로 JUMP

_up:
	cmp	r9, r8	
	je	_down	;	r9과 r8을 비교하여 같으면 _down 함수로 JUMP
	mov 	rsi, LF	;	write 출력 문자 = '\n' 설정
	syscall
	mov	rax, 1	;	write 함수 설정
	mov	r10, 0	;	r10 0으로 초기화
	inc	r9	;	r9 1 증가
	jmp	_small	;	small 함수로 JUMP

_down:
	cmp	r9, 0
	je	_done	;	r9과 0을 비교하여 같으면 _done 함수로 JUMP
	mov 	rsi, LF	;	write 출력 문자 = '\n' 설정
	syscall
	
	mov	rax, 1	;	write 함수 설정
	
	mov	r10, 0	;	r10 0으로 초기화
	dec	r9	;	r9 1 감소
	
	jmp	_big	;	_big 함수로 JUMP

_big:
	cmp	r10, r9
	je	_down	;	r10과 r9을 비교하여 같으면 _down 함수로 JUMP
	mov	rsi, STAR;	write 출력 문자 = '*' 설정
	syscall

	mov	rax, 1	;	write 함수 설정
	
	inc	r10	;	r10 1 증가
	
	jmp	_big	;	_big 함수로 JUMP

_done:
	mov	rax, 60
	mov	rdi, 0
	syscall
	;	exit 함수 설정 및 호출하여 프로그램 종료

_syscall:
	syscall		;	모든 레지스터 데이터를 스택에 저장
	ret		;	EIP에 저장된 주소로 되돌아간다.
