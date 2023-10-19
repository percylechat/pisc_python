import sys

if len(sys.argv) < 2:
    sys.exit(0)
try:
    assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
except AssertionError as msg:
    print(msg)
    sys.exit(1)
if sys.argv[1]:
    try:
        assert sys.argv[1].isdigit(), "AssertionError: argument is not an integer"
    except AssertionError as msg:
        print(msg)
        sys.exit(1)
if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")