from colorama import init
from colorama import Fore, Back, Style
init()

EMPTY_SPACE = " " * 4
EDGE = "--- "
CROSS = "+"
FINAL_CROSS = "\\"
THERE_IS_MORE = "..."

def print_tree(db, s):
    db['scanned'] = []
    print(recursive_print(db, 0, s))

def recursive_print(db, indent_num, url):
    if url in db['scanned']:
        if db[url]['color'] == "red":
            return Fore.RED+url+Style.RESET_ALL+Fore.YELLOW+THERE_IS_MORE+Style.RESET_ALL
        if db[url]['color'] == "green":
            return Fore.GREEN+url+Style.RESET_ALL+Fore.YELLOW+THERE_IS_MORE+Style.RESET_ALL
    db['scanned'] += [url]
    ret = ""
    if db[url]['color'] == "red":
        ret = Fore.RED + url +Style.RESET_ALL+ "\n"
    else:
        ret = Fore.GREEN + url +Style.RESET_ALL+ "\n"
    for child in db[url]['children'][:-1]:
        ret += EMPTY_SPACE*indent_num+CROSS+EDGE
        ret += recursive_print(db, indent_num + 1, child)
        ret += "\n"
    if len(db[url]['children']) > 0:
        ret += EMPTY_SPACE * indent_num + FINAL_CROSS + EDGE
        ret += recursive_print(db, indent_num + 1, db[url]['children'][-1])
    return ret
