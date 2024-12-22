import browser_cookie3

cookies = browser_cookie3.edge(domain_name='youtube.com')

with open('cookies.txt', 'w') as f:
    for cookie in cookies:
        f.write(
            f"{cookie.domain}\t"
            f"{'TRUE' if cookie.secure else 'FALSE'}\t"
            f"{cookie.path}\t"
            f"{'TRUE' if cookie.secure else 'FALSE'}\t"
            f"{cookie.expires}\t"
            f"{cookie.name}\t"
            f"{cookie.value}\n"
        )
print("Cookies экспортированы в cookies.txt")
