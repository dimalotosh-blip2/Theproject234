import colorama
from colorama import Fore, Back, Style

colorama.init()  # запускає підтримку кольорів у консолі

print(Fore.RED + "Hello")      # колір тексту
print(Back.GREEN + "Hello")       # колір фону
print(Style.BRIGHT + "Hello")      # стиль тексту

colorama.deinit()  # вимикає кольори після завершення
