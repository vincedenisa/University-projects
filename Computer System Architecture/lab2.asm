bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

segment data use32 class=data
    a db 2          ; Example value for a (byte)
    b db 3          ; Example value for b (byte)
    c db 5          ; Example value for c (byte)
    d dw 10         ; Example value for d (word)

segment code use32 class=code
    start:
        
        
    ; 1. 1 + 9
    mov al, 1       ; Load 1 into AL
    add al, 9       ; AL = AL + 9
    ; Result in AL (10)

    
    
    ; 2. c - (a + d) + (b + d)
    mov al, [c]     ; Load c into AL
    mov bl, [a]     ; Load a into BL
    add bl, [d]     ; BL = a + d
    sub al, bl      ; AL = c - (a + d)
    
    mov bl, [b]     ; Load b into BL
    add bl, [d]     ; BL = b + d
    add al, bl      ; AL = (c - (a + d)) + (b + d)
    ; Result in AL

    
    
    ; 3. (c + b + a) - (d + d)
    mov ax, [c]     ; Load c into AX
    add ax, [b]     ; AX = c + b
    add ax, [a]     ; AX = c + b + a

    mov bx, [d]     ; Load d into BX
    shl bx, 1       ; BX = d + d (multiply by 2)
    sub ax, bx      ; AX = (c + b + a) - (d + d)
    ; Result in AX

   

   ; 4. ((a + b - c) * 2 + d - 5) * d
    mov al, [a]     ; Load a into AL
    add al, [b]     ; AL = a + b
    sub al, [c]     ; AL = (a + b) - c

    ; Multiply by 2
    shl ax, 1       ; AX = (a + b - c) * 2

    add ax, [d]     ; AX = ((a + b - c) * 2) + d
    sub ax, 5       ; AX = (((a + b - c) * 2) + d) - 5

    ; Multiply by d
    imul ax, [d]    ; AX = (((a + b - c) * 2) + d - 5) * d
    ; Result in AX

    
    
    ; 5. ((a - b) * 4) / c
    mov al, [a]     ; Load a into AL
    sub al, [b]     ; AL = a - b
    shl ax, 2       ; AX = (a - b) * 4

    ; Divide by c
    xor dx, dx      ; Clear DX for division
    mov cx, [c]     ; Load c into CX
    idiv cx         ; AX = ((a - b) * 4) / c
    ; Result in AX

    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
