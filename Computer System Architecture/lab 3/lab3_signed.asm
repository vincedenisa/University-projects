bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db -1
    b dw 2
    c db 5
    d dd -1
    x dq 8
    r resq 1
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        mov ebx, 7
        mov al, [a]
        cbw
        imul WORD[b]; eax=a*b
        push DX
        push AX
        pop EAX; push dx and ax onto the stack and pop them into eax
        sub ebx, eax; ebx = ebx-eax
        mov al, [c]
        cbw
        cwd
        push DX
        push AX
        pop EAX
        add ebx, eax ; ebx = (7-a*b+c)
        mov ecx, ebx ;ecx = (7-a*b+c)
        mov al, [a]
        cbw
        mov bx, ax
        mov eax, ecx
        idiv bx ; ax = (7-a*b+c)/a
        cwd
        push DX
        push AX
        pop EAX
        mov ebx, eax ; ebx = (7-a*b+c)/a
        mov eax, [d]
        sub eax, ebx
        sub eax, 6 ;eax = d-(7-a*b+c)/a-6
        mov [r], eax ;r = d-(7-a*b+c)/a-6
        mov eax, dword[x+0]
        mov edx, dword[x+4]
        mov ebx, 2
        idiv ebx
        add [r], eax ; r = d-(7-a*b+c)/a-6+x/2
        mov eax, 0
        mov eax, [r]
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program