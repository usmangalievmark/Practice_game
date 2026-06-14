from time import sleep


def dialogue_delay(func):
    def wrapper(text):
        func(text)
        sleep(2)
    return wrapper

@dialogue_delay
def game_print(text):
    print(text)