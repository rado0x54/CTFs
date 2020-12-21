What does asm2(0x4,0x21) return?
- Explanations in comments
- Note:
  - ebp+0x8 points to the function argument `0x4`
  - ebp+0xc points to the function argument `0x21`

```asm
asm2:
<+0>:	push   ebp                        1. Push current ebp to the sack
<+1>:	mov    ebp,esp                    2. Save esp in ebp 
<+3>:	sub    esp,0x10                   3. esp -= 0x10 (space for locals)
<+6>:	mov    eax,DWORD PTR [ebp+0xc]    4. eax = 0x21
<+9>:	mov    DWORD PTR [ebp-0x4],eax    5. local_a = 0x21
<+12>:	mov    eax,DWORD PTR [ebp+0x8]    6. eax = 0x4
<+15>:	mov    DWORD PTR [ebp-0x8],eax    7. local_b = 0x4
<+18>:	jmp    0x509 <asm2+28>            -> fixed jump
<+20>:	add    DWORD PTR [ebp-0x4],0x1    9a: local_a++
<+24>:	add    DWORD PTR [ebp-0x8],0x74   9b: local_b += 0x74
<+28>:	cmp    DWORD PTR [ebp-0x8],0xfb46 8a. -> CMP local_b <= 0xfb46
<+35>:	jle    0x501 <asm2+20>            8b. JUMP if 8a TRUE. 
<+37>:	mov    eax,DWORD PTR [ebp-0x4]    10. return local_a
<+40>:	leave  
<+41>:	ret 
```
- Loop is exectued `0x22b` times: `(0xfb46 - 0x4) / 0x74 == 0x22a` (1+ for `<=`)
- `local_a = 0x21 + 0x22b = 0x24c`

Flag: 0x24c