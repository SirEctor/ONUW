import webbrowser, bs4, requests
from selenium import webdriver
if __name__ == "__main__":
    print("")
    #credit - https://stackoverflow.com/questions/832331/launch-a-webpage-on-a-firefox-win-tab-using-python
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

    print("\nReady to Join!")
    joinCode = input("Enter join code:\n")
    firefox.open_new_tab("https://werewolf.invades.space/")

