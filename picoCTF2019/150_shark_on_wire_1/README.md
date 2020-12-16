Use Wireshark to inspect the given stream:

- We are looking for a `}` character in the stream, so we can narrow down 
  the search by filtering `udp contains '}' || tcp contains '}'`
  
- There are exactly two distinct UDP matches. One stream contains `picoCTF{N0t_a_fLag}`
  the other one has the correct flag of `picoCTF{StaT31355_636f6e6e}`
