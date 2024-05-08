import os
import github
import colorama
import accounts
import instabot
import time

owner = {"name": "natrix"}
github_url = "https://github.com/natrixdev"
requirements = "https://github.com/natrixdev/instagram-botter/blob/main/reqs.txt"
owner_repos = "https://github.com/natrixdev?tab=repositories"
how_to_use = "https://github.com/natrixdev/instagram-botter/blob/main/README.md"
this_code = "https://github.com/natrixdev/instagram-botter/blob/main/main.py"

os.system("title Instagram followers, likes and views botter.")
colorama.init(autoreset=True)

def main():
    account_name = input("Account name? ")
    if account_name == "":
        print('Please input a real name')
    elif not req_on(f"https://www.instagram.com/{account_name}/"):
        print("I didn't find your Instagram account.")
        print("Please choose a botter category:")
        print("[1] - Likes")
        print("[2] - Views")
        print("[3] - Followers")
        choose = input('> ')
        if choose == "1":
            url = input('Paste your Instagram post URL (your account needs to be public): ')
            if not req_url(url):
                print('Cannot find the post.')
            else:
                acc_num = 1
                while True:
                    accounts.newInstagram('goto --like %url%')
                    acc_num += 1
                print(str(acc_num) + " likes done.")
        elif choose == "2":
            url = input("Please input your story URL (needs to be public and can be found on Instagram's computer version): ")
            if not req_url(url):
                print('Cannot find the story/account.')
            else:
                req_url(f"https://www.instagram.com/stories/{account_name}/{url}/")
                req_new_accounts()

                # def gen():
                #     accounts.newInstagrams(forViews)

        elif choose == "3":
            print("Welcome to the followers botter for Instagram.")
            # Remove PayPal donation message
            print("No donation required.")
            # Remove PayPal check
            # if btc_check_for_transac("local --ip & paypal.com/me"):
            print('Welcome to the gen.')
            code_access('repl.fllwrs-code')
            # else:
            #     print('Money not on this account - Followers gen is locked for 24hrs on your machine.')
            #     huy = time.time() + 24 * 3600
            #     time_to_wait = huy - time.time()
            #     file_lock(time_to_wait)
    else:
        print('Money not on this account - Followers gen is locked for 24hrs on your machine.')
        huy = time.time() + 24 * 3600
        time_to_wait = huy - time.time()
        file_lock(time_to_wait)
    gen = main()
    # url = req()
    # usages = req("https://github.com/natrixdev/")

def req_on(url):
    # Logic for checking if the Instagram account exists
    pass

def req_url(url):
    # Logic for checking if the URL is valid
    pass

def req_new_accounts():
    # Logic for creating new Instagram accounts
    pass

def btc_check_for_transac(payment_info):
    # Logic for checking Bitcoin transactions
    pass

def code_access(code):
    # Logic for accessing code
    pass

def file_lock(time_to_wait):
    # Logic for file locking
    pass

if __name__ == "__main__":
    main()
