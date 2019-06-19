def header():
    print("CASH RECEIPT")


def dashes():
    print("------------------------------")


def body():
    print("Charged to____________________\nReceived by___________________")


def footer():
    print("© SoftUni")


def print_receipt():
    header()
    dashes()
    body()
    dashes()
    footer()


if __name__ == "__main__":
    print_receipt()