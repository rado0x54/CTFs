asm3:
    push   ebp
    mov    ebp,esp
    xor    eax,eax
    mov    ah,BYTE PTR [ebp+0x9]
    shl    ax,0x10
    sub    al,BYTE PTR [ebp+0xe]
    add    ah,BYTE PTR [ebp+0xf]
    xor    ax,WORD PTR [ebp+0x12]
    nop
    pop    ebp
    ret

