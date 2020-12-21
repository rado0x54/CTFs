What does asm3(0xd2c26416,0xe6cf51f0,0xe54409d5) return?
- Explanations in comments
- Note:
  - ebp+0x4 points to `return address`
  - ebp+0x8 points to the function argument `0xd2c26416`
  - ebp+0xc points to the function argument `0xe6cf51f0`
  - ebp+0x10 points to the function argument `0xe54409d5`

```asm
asm3:
<+0>:	push   ebp
<+1>:	mov    ebp,esp
<+3>:	xor    eax,eax                1. Set eax = 0  eax: 0x00000000
<+5>:	mov    ah,BYTE PTR [ebp+0x9]  2. ah = 0x64:   eax: 0x00006400
<+8>:	shl    ax,0x10                3. ax << 2      eax: 0x00009000
<+12>:	sub    al,BYTE PTR [ebp+0xe]  4. al -= 0xcf   eax: 0x00009031
<+15>:	add    ah,BYTE PTR [ebp+0xf]  5. ah += 0xe6   eax: 0x00007631
<+18>:	xor    ax,WORD PTR [ebp+0x12] 6. ax ^= 0xe544 eax: 0x00009375
<+22>:	nop
<+23>:	pop    ebp
<+24>:	ret    
```
- Loop is exectued `0x22b` times: `(0xfb46 - 0x4) / 0x74 == 0x22a` (1+ for `<=`)
- `local_a = 0x21 + 0x22b = 0x24c`

Flag: 0x24c