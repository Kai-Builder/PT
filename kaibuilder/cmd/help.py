import kaibuilder.utility as util
a = 30


def main(args: list[str]):
    if util.sizeof(args) == 0: return
    print("Now you have an argument")


