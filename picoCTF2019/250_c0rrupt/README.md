- Let's print the head of the file to discover some information:
```shell
00000000  89 65 4e 34 0d 0a b0 aa  00 00 00 0d 43 22 44 52  |.eN4........C"DR|
00000010  00 00 06 6a 00 00 04 47  08 02 00 00 00 7c 8b ab  |...j...G.....|..|
00000020  78 00 00 00 01 73 52 47  42 00 ae ce 1c e9 00 00  |x....sRGB.......|
00000030  00 04 67 41 4d 41 00 00  b1 8f 0b fc 61 05 00 00  |..gAMA......a...|
```
- The `sRGB` seems to point to an image/video format so let's look at
  some header formats found [here](https://en.wikipedia.org/wiki/List_of_file_signatures)
  
```shell
current : 89 65 4e 34 0d 0a b0 aa
PNG     : 89 50 4e 47 0d 0a 1a 0a
```
- Let's fix the header with:
```shell
  cp mystery mystery_fixed.png && \
  echo -ne \\x89\\x50\\x4E\\x47\\x0D\\x0A\\0x1A\\0x0A \
  | dd conv=notrunc bs=1 count=8 of=mystery_fixed.png
```
- Still, no luck, so let's understand the PNG data format a little better: 
  [Link](https://www.oreilly.com/library/view/png-the-definitive/9781565925427/17_chapter-08.html)

- "A valid PNG image must contain an IHDR chunk, one or more IDAT chunks, and an IEND chunk." 
  [source](http://www.libpng.org/pub/png/spec/1.1/PNG-Chunks.html)
  
```shell
(venv) % strings mystery_fixed.png| grep IEND
IEND
(venv) % strings mystery_fixed.png| grep IDAT
IDAT6
IDAT
IDAT
(venv) % strings mystery_fixed.png| grep IHDR
```
- Missing IDHR: Fix first "chunk" unitl (4-bytes + 'sRGB'):
```shell
00 00 00 0D <- length (13)
43 22 44 52 <- type (should be IHDR)
00 00 06 6A 
00 00 04 47 
08 02 00 00 
00 
7C 8B AB 78  <- CRC      
```
- CRC via [crccal.com](https://crccalc.com/?crc=49 48 44 5200 00 06 6A 00 00 04 47 08 02 00 00 00&method=crc32&datatype=hex&outtype=hex)
  `0x7C8BAB78` -> correct
- Still does not work.
- Check file with tool:
```shell
% pngcheck mystery_fixed.png
mystery_fixed.png  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERROR: mystery_fixed.png
```
- The following type `.DET (AB 44 45 54)` seems wrong, so let's assume `IDAT` 
- Fixed pHYs CRC, but saw that length of the following chunk `IDAT` with `1162128293 (AA AA FF A5)`
can also not be correct.
  
- The next `IDAT` starts at `0x10008`, e.g. the chunk ends at `0x10004` and the
  data at `0x10000`. The previous `IDAT` segment starts at `0x5b`. Difference is `0xFFA5`

- After this, all is good:
```shell
% pngcheck mystery_fixed.png
OK: mystery_fixed.png (1642x1095, 24-bit RGB, non-interlaced, 96.3%).
```
Flag: `picoCTF{c0rrupt10n_1847995}`
