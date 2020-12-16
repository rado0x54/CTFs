Following command(s) will find the flag:

    # Look at robots.txt (https://en.wikipedia.org/wiki/Robots_exclusion_standard)
    curl https://jupiter.challenges.picoctf.org/problem/36474/robots.txt
    User-agent: *
    Disallow: /477ce.html

    # Checkout disallowed file:
    curl https://jupiter.challenges.picoctf.org/problem/36474/477ce.html | gsed -n 's/.*<flag>\(.*\)<\/flag>.*/\1/p'

    picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
