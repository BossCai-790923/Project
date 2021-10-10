import sys

for line in sys.stdin:

    line = line.rstrip()
    print(f"You input: {line}")

# IMPORTANCE !! ----------------------------------
# Q) What is sys.stdin?
# A) sys.stdin is a file. Whatever you input to the console, the content will be saved to the sys.stdin file.
#    so you can loop all the lines in the file:
#    for line in sys.stdin:
#       loop_body
#
# Q) What is rstrip()?
# A) line variable always contain line_return character (\n)
#    line.rstrip() will remove the empty space & line_return character at the end of the line variable.
#
# In summary, sys.stdin() is quite similar to input()
# ------------------------------------------------

