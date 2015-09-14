%ifndef CDC
	%define CDC  
	section .bss
		%ifndef TRUE
			TRUE	equ 1
		%endif
		%ifndef FALSE
			FALSE	equ 0
		%endif	
	
		%macro END	0
			XOR		EAX, EAX
			MOV 	EAX, 1
			XOR		EBX, EBX
			INT		0x80		
		%endmacro
		
		%ifdef x64
			RSIZE	equ	8
		%else
			RSIZE	equ 4
		%endif
		
		%define x0 EAX
		%define x1 ECX
		%define x2 EDX
		%define x3 EBX
		%define x4 ESP
		%define x5 EBP
		%define x6 ESI
		%define x7 EDI
	
		%define x0_L AL
		%define x1_L CL
		%define x2_L DL
		%define x3_L BL
		
		%define x0_H AH
		%define x1_H CH
		%define x2_H DH
		%define x3_H BH
		
		%ifdef x64
			%define r0 RAX 
			%define r1 RCX
			%define r2 RDX
			%define r3 RBX
			%define r4 RSP
			%define r5 RBP
			%define r6 RSI
			%define r7 RDI
		%else
			%define r0 x0
			%define r1 x1
			%define r2 x2
			%define r3 x3
			%define r4 x5
			%define r6 x6
			%define r7 x7
		%endif
		
		%macro PuFS 0
			push	r3
			push	r5
			push	r6
			push	r7
		%endmacro
		%macro PoFS 0
			pop		r3
			pop		r5
			pop		r6
			pop 	r7
		%endmacro
%endif
