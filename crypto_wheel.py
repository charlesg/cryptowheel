#! /usr/local/bin/python2.7

# Encrypt a string based on the cryptowheel
# currently only supports UPPERCASE strings.

import getopt
import sys
import string

__author__="cgagnon"
__date__ ="$Dec 1, 2010 10:49:21 AM$"

def usage():
	   print sys.argv[0] + " -h --key=KEY --text=STRING -e -d"

def rotate_string(alpha,spaces):
    letters = ['']
    for c in alpha:
        a = ord(c) - 65
        a = (a + spaces)%26 + 65
        a = chr(a)
        letters.append(a)
    return ''.join(letters)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ht:k:ed", ["help", "text=", "key=", "encrypt", "decrypt"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    text = "DEFAULT STRING"
    encrypt = False
    decrypt = False
    for o, a in opts:
        if o in ("-e", "--encrypt"):
            if decrypt == True:
                assert False, "Cannot decrypt and encrypt at the same time"
            else:
                encrypt = True
        elif o in ("-d", "--decrypt"):
            if encrypt == True:
                assert False, "Cannot decrypt and encrypt at the same time"
            else:
                decrypt = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-t", "--text"):
            text = a
        elif o in ("-k", "--key"):
            key = a
        else:
            assert False, "unhandled option"

    # The source of the translation, the letters of the alphabet.
    #letters = string.ascii_lowercase + string.ascii_uppercase
    letters = string.ascii_uppercase

    try:
        if (len(key) == 1):
            # Key is "White in front of Blue Q"
            spaces =  ord(key) - ord("A")
            letters = rotate_string(letters, spaces) 
        else:
            usage()
            sys.exit()
    except:
            usage()
            sys.exit()


    # I need my crypto-wheel setup
    #trans_table = "qjrbsktuclvgwdxhmenyzaoipfQJRBSKTUCLVGWDXHMENYZAOIPF"
    trans_table = "QJRBSKTUCLVGWDXHMENYZAOIPF"
    trans = None
    
    #resp = raw_input("Encrypt or decrypt? ")

    if encrypt == True:
        # encrypt
        trans = string.maketrans(trans_table,letters)
        print "Clear    : " + text
        print "Encrypted: " + text.translate(trans)
    elif decrypt == True:
        # decrypt
        trans = string.maketrans(letters,trans_table)
        print "Encrypted: " + text
        print "Clear    : " + text.translate(trans)
    else:
        # encrypt
        trans = string.maketrans(trans_table,letters)
        print "Clear    : " + text
        print "Encrypted: " + text.translate(trans)



if __name__ == "__main__":
    main(sys.argv[1:])
