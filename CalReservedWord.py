reWords = {"False","def","if","raise","None","del","import","return","True","elif","in","try","and","else","is","while","as","except",
    "lambda","with","assert","finally","nonlacal","yield","break","for","not","class","from","or","continue","global","pass"}
def getText():
    txt = open("Text.txt","r",errors='ignore').read()
    for ch in '":#+-*/.,;=(){\\}[]|!^?':
        txt = txt.replace(ch, " ")
    return txt
def countWords():
    programText = getText()
    words = programText.split()
    counts = {}
    for word in words:
        if word in reWords:
            counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    for i in range(33):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
def main():
    countWords()
if __name__ == "__main__":
    main()