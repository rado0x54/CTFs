Following command will find the flag within the code:

    # Download webpage source
     wget --recursive --no-directories --html-extension --page-requisites --convert-links --no-parent https://jupiter.challenges.picoctf.org/problem/41511/

    # Rebuild flag (note, \S requires gnu-sed)
     cat * | gsed -n 's/^.*flag: \(\S*\) .*$/\1/p' | tr -d '\n'

    picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}
