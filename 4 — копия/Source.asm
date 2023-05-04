.586 
.MODEL flat,C
.DATA

SUM DD 0.0
i_local DD 1
n dd 0

.CODE

extern fun_el:near ; объявлениевнешнейфункцииfun_el
public SumR
SumR proc C
		push ebp;
		mov ebp,esp;
		mov i_local, 0;
		mov ecx, dword ptr [ebp+8];
		mov n, ecx;

	;начало цикла
		L1:
				push dword ptr [ebp + 12]
				push i_local
				call fun_el
				fld SUM
				fadd
				fstp SUM
		;проверка условия на конец цикла
				mov ecx, i_local;
				inc ecx;
				mov i_local, ecx;
				mov eax, n;
				add eax, 1;
				cmp ecx, eax;
				jne L1;

;конеццикла
fld SUM
mov esp,ebp
pop ebp

ret
SumR endp
End
