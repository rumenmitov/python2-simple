import sys
import platform

if sys.version_info[0] != 2:
    sys.stderr.write("This script requires Python 2\n")
    sys.exit(1)

def main():
    print("This is Python " + platform.python_version())
    d = {1: "one", 2: "two"}
    for k, v in d.iteritems():
        print(k, v)
    big = 12345
    print("long: " + str(big))

if __name__ == "__main__":
    main()
