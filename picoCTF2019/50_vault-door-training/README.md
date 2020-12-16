Following command will find the flag within the code:

    cat VaultDoorTraining.java | grep "password.equals" | awk -F \" '{ print "picoCTF{"$2"}" }'

    picoCTF{w4rm1ng_Up_w1tH_jAv4_eec0716b713}
