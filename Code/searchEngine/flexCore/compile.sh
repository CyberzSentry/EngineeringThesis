#!/bin/bash
echo "Compiling flex core.l"
echo $(flex core.l)
echo "Compiling the output c code"
echo $(gcc lex.yy.c -o core)
echo "Setting the proper file premisions"
echo $(chmod +x ./core)
