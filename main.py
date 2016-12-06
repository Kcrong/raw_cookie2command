import sys

print("Domain Ex) .naver.com")

if sys.version_info.major == 3:
    domain = input("Domain: ")
else:
    domain = raw_input("Domain: ")


cookie_command = ""

try:
    f = open("input_cookie.txt", "r")
except IOError:
    print("where is 'input_cookie.txt' ?")
else:
    raw_cookies = f.read()

    for cookie in raw_cookies.split(';'):
        eq_index = cookie.find('=')

        cookie_command += 'document.cookie="%s=%s";domain="%s";path="/";' % (cookie[:eq_index], cookie[eq_index + 1:], domain)

    print("------------------------------------")
    print(cookie_command[:-1])
    with open("output_cookie.txt", "w") as f:
        f.write(cookie_command)
    print("\n\n")
    print("By Kcrong :)")
