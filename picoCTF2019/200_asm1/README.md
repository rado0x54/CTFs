- What does asm1(0x6fa) return?
- Explanations in comments
- Note:
  - ebp+0x8 points to the function argument `0x6fa`

```asm
asm1:
	<+0>:	push   ebp                        # 1. push ebp on the stack
	<+1>:	mov    ebp,esp                    # 2. copy esp into ebp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3a2  # 3. cmp 0x6fa, 0x3a2
	<+10>:	jg     0x512 <asm1+37>            # 4. JUMP: 0x6fa >s 0x3a2 -> TRUE
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x358
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x12
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0x12
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x6fa  # 5. cmp 0x6fa, 0x6fa
	<+44>:	jne    0x523 <asm1+54>            # 6. NO JUMP: 0x6fa != 0x6fa -> FALSE
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]    # 7. mov 0x6fa into eax
	<+49>:	sub    eax,0x12                   # 8. eax: 0x6fa - 0x12 = 0x6e8
	<+52>:	jmp    0x529 <asm1+60>            # 9. JUMP
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0x12
	<+60>:	pop    ebp                        # 10. pop ebp from the stack
	<+61>:	ret                               # 11. ret with eax: 0x6e8
```
Flag: 0x6e8