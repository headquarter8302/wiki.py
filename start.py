import json

class colors:
  FAIL    = "\033[91m"
  MESSAGE = '\033[93m'
  NORMAL  = "\033[0m"
  OKGREEN = "\033[92m"
  
siteInfo      = open("wikiInfo.json")
site          = json.load(siteInfo)
pagesDatabase = open("database.json")
pages         = json.load(pagesDatabase)
bannedWords   = open("bannedWords.json")
banned        = json.load(bannedWords)

for i in site["wikiInfo"]:
  if i["wikiName"] == "wiki.py":
    print(colors.NORMAL + "###################################################")
    print("# __          _______ _  _______   _______     __ #")
    print("# \ \        / /_   _| |/ /_   _| |  __ \ \   / / #")
    print("#  \ \  /\  / /  | | | ' /  | |   | |__) \ \_/ /  #")
    print("#   \ \/  \/ /   | | |  <   | |   |  ___/ \   /   #")
    print("#    \  /\  /   _| |_| . \ _| |_ _| |      | |    #")
    print("#     \/  \/   |_____|_|\_\_____(_)_|      |_|    #")
    print("#                                                 #")
    print("###################################################")
    print("")
    print("Welcome to the startup script! In here, you would configure")
    print("your installation of wiki.py to your needs")
    print("")
    def askWikiName():
      wikiname = input("First off, what is your wiki name?")
      for bannedWord in banned["bannedWords"]:
        if bannedWord in wikiname:
          return print(colors.FAIL + "Wikiname contains a banned word.")
        if wikiname != bannedWord:
          print(colors.OKGREEN + "Great, your wiki now have a name!")
          def writePage(newData, filename="wikiInfo.json"):
            with open(filename, "r+") as file:
              file_data = json.load(file)
              file_data["wikiPage"].append(newData)
              file.seek(0)
              json.dump(file_data, file, indent=2)
              y = {
                "wikiPageName": pageName,
                "wikiPageContent": pageContent,
          "isLocked": "False"
              }
              writePage(y)
              else:
                print(colors.NORMAL + "You have already configured this install of wiki.py, to change the configuration, edit wikiInfo.json")
