import sys
import platform

if sys.version_info[0] != 2:
    sys.stderr.write("This script requires Python 2\n")
    sys.exit(1)

def main():
    # Python-2-only: print statement syntax (SyntaxError on Python 3)
    print "This is Python", platform.python_version()
    d = {1: "one", 2: "two"}
    # Python-2-only: dict.iteritems() removed in Python 3
    for k, v in d.iteritems():
        print k, v
    # Python 2 long literal suffix
    big = 12345L
    print "long:", big

if __name__ == "__main__":
    main()
