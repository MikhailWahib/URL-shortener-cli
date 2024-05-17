import requests
import os
import getpass


def clear_screen():
    curOs = os.name

    if curOs == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear_screen()

print("|---------------------------------------------|")
print("|         Welcome to URL Shortener            |")
print("|                                             |")
print("|        For registration, go to:             |")
print("|                                             |")
print("| https://url-shortener-mw.vercel.app/signup  |")
print("|---------------------------------------------|")
print("\n Note: Server may take some time to respond for the first time, please wait ...")
print("\n Please enter your credentials: ")
username = input("\n username: ")
password = getpass.getpass(" password: ")

clear_screen()

print("Loading ...")

login_res = requests.post("https://url-shortener-api-56k6.onrender.com/api/v1/users/login",
                          json={"username": username, "password": password})

if login_res.status_code != 200:
    print("Login Failed")
    exit()

clear_screen()

token = login_res.cookies.get("jwt")

print("Login Successful")


def shorten_url():
    url = input("Enter URL: ")
    shorten_url_res = requests.post(
        "https://url-shortener-api-56k6.onrender.com/api/v1/shorten", json={"url": url}, cookies={"jwt": token})
    shorten_url = shorten_url_res.json()["shortUrl"]
    print(f"Shortened URL: {shorten_url}")
    input("\n Press Enter to return to the menu \n")


def show_shortened_urls():
    user_urls_res = requests.get(
        "https://url-shortener-api-56k6.onrender.com/api/v1/users/urls", cookies={"jwt": token})
    if user_urls_res.status_code != 200:
        print("No shortened URLs found")
        input("\n Press Enter to return to the menu \n")
        return
    user_urls = user_urls_res.json()["urls"]

    for url in user_urls:
        print("----------------------------------")
        print(f"Original URL: {url['originalUrl']}")
        print(f"Short URL: {url['shortUrl']}")
    input("\n Press Enter to return to the menu \n")


while True:
    clear_screen()

    print("1. Shorten URL")
    print("2. Show Shortened URLs")
    print("3. Exit")

    option = int(input("Enter option: "))

    if option == 1:
        shorten_url()
    elif option == 2:
        show_shortened_urls()
    elif option == 3:
        exit()
