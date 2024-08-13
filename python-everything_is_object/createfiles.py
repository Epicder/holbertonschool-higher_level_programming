def createfiles():
    for i in range(28):
        filename = str(i) + "-answer" + ".txt"
        file = open(filename, "w")
        file.write("")
        file.close()
    return

if __name__ == "__main__":
    createfiles()
