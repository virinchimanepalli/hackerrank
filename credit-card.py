#need to analysis
import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
# for _ in range(int(input().strip())):
print("Valid" if TESTER.search("4253625879615786") else "Invalid")