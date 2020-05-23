import re

k = "virinchi.msk82@gmail.com"

b = "britts_54@hackerrank.com"
a = re.match(r'[a-zA-z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',b)
# print(a)
if a is None:
    print("not")
else:
    print("value")



#hackerranksolution:
def fun(s):
    # return True if s is a valid email, else return False
    import re
    a = re.match(r'[a-zA-z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    if a is None:
        return False
    else:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)