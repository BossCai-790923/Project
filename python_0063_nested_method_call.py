animals=['tiger','elephant','snake','shark']
#python do 'swich'
#it appends(0) to the end use(pop)
# IMPORTANCE!!! ----------------------------------------------------
# python code runs from top line to bottom line.
# in the same line, python runs from left to right.
# Here python notice, it needs to append something at the end of the animals list
# But python tries figuring out what it should append, it notices it is another method call.
# So append method will PAUSE
# python will first call animals.pop(0), 'tiger' will be popped out, returned as the value to be appended
# then append method finishes.
# ------------------------------------------------------------------
animals.append(animals.pop(0))
print(animals)