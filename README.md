# Crypto-Wheel Project

This will allow you to automatically encrypt or decrypt a text based
on the man-made Crypt-Wheel. When using the physical wheel, always
encrypt from BLUE to WHITE and decrypt from WHITE to BLUE. Make sure
to properly set the wheel to the KEY.

The script currently supports UPPERCASE letters only.

The KEY is set by indicating the letter in WHITE, lined up with the
BLUE letter "Q".

Example:

```
$ ./crypto_wheel.py --key=A --text="THIS IS MY STRING" -e 
Clear    : THIS IS MY STRING
Encrypted: GPXE XE QT EGCXSL

$ ./crypto_wheel.py --key=A --text="GPXE XE QT EGCXSL" -d 
Encrypted: GPXE XE QT EGCXSL
Clear    : THIS IS MY STRING
```

--
December 10th 2010
Charles Gagnon, charlesg@unixrealm.com
