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
    a db -6
    b dw -10
    c dd 3
    d dq 5
    r resq 1
    
; our code starts here
segment code use32 class=code
    start:
        mov ax, [b]; => ax = -10
        cwd ; converts the signed value in ax to a signed value in dx:ax
        
        push DX
        push AX
        pop EAX ; push dx and ax onto the stack, then pops them into eax
        
        add eax,[c] ; => eax = b+c
        cdq
        add eax, dword[d+0]; adds the lower part of d to eax
        adc edx, dword[d+4]; edx:eax = b + c + d
        
        mov dword[r+0], eax
        mov dword[r+4], edx ; r = b + c + d => store the result from eax into the first half of r and edx onto the second
        
        mov al, [a]
        cbw
        cwd
        push DX
        push AX
        pop EAX
        cdq ; push dx and ax onto the stack, pop them into eax, so eax holds the sign-extended value of a
        
        add dword[r+0], eax ; adds the value in eax to the first 4 bytes of r
        add dword[r+4], edx ; r = b + c + d + a
        
        mov ebx, dword[d+0]; loads the first 4 bytes of d into ebx
        mov ecx, dword[d+4]; loads the second 4 bytes of d into ecx
        
        mov eax, dword[c]
        cdq; loads the value of c into eax and sign-extends it into edx
        
        add eax, ebx; => eax = eax+ebx
        add edx, ecx; eax:edx = (d+c)
        
        sub dword[r+0], eax; substracts eax from the first part of r
        sbb dword[r+4], edx ; r = b + c + d + a - (d+c)
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program