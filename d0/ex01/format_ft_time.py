from time import time, gmtime, strftime

now = round(time(), 4)
print("Seconds since January 1, 1970: "f"{now:,} or "f"{now:.2E} in scientific notation")
print(strftime("%b %d %Y", gmtime()))
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$