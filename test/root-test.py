RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RESET='\033[0m'

def good(msg):
    return f"{GREEN}{msg}{RESET}"

def bad(msg):
    return f"{RED}{msg}{RESET}"

def info(msg):
    return f"{BLUE}{msg}{RESET}"

def testEqual(msg, x, y, results):
    (ntests, nfails) = results
    if(x == y):
        print(f"  {msg} ... {good('PASS')}")
        return (ntests + 1, nfails)
    else:
        print(f"  {msg} ... {bad('FAIL')}")
        return (ntests + 1, nfails + 1)

def printMsg(msg, x):
    print(info(msg))
    return x

def printResult(x):
    if(x[1] == 0):
        print(good(f"All {x[0]!s} tests pass"))
    else:
        print(bad(f"{x[1]!s}/{x[0]!s} tests failed"))
    return x
