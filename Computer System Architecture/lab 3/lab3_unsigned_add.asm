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
    a db 1
    b dw 2
    c dd 3
    d dq 5
    r resq 1
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov eax, 0
        mov edx, 0
        mov al, [a]; edx:eax = a
        
        mov ebx, dword[d+0]; loads the first 4 bytes of d  into ebx
        mov ecx, dword[d+4]; loads the next 4 bytes of d into ecx
        add eax, ebx ; => eax = 6
        adc edx, ecx; edx: eax = a + d = 6
        
        add eax, ebx ; => eax = 11
        adc edx, ecx; edx:eax = a + d + d
        
        mov ebx, dword[c] ; => ebx = 3
        mov ecx, 0
        
        sub eax, ebx ; => eax = 8
        sbb edx, ecx; edx:eax = (a + d + d) - c       
        
        mov dword[r+0], eax ; loads the lower 4 bytes of r in the first 4 bytes 
        mov dword[r+4], edx ; loads edx (0) in the next 4 bytes => r = (a + d + d) - c       
        
        mov eax, 0
        mov ax, [b]; => ax = 2
        mov edx, 0
        add ax, [b] ; edx: eax = (b + b) => eax = 4
        
        add dword[r+0], eax ;  adds the value of eax (4) to the first 4 bytes of r => r now containing 12 in the first half
        adc dword[r+4], edx; r = (a + d + d) - c + (b + b)
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program