from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.RED + 'красний текст')
print(Back.BLACK + 'на черном фоне')
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')