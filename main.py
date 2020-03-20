def readin(filename: str):
    with open(filename) as f:
        content = f.read().splitlines()
    return content

def contains(arr, word):
    for i in range(0, len(arr)):
        spltln = arr[i].split("|")
        for x in spltln:
            if(x.__contains__(word)):
                return (True, i)
    return False

def replace(line, word):
    spltln = line.split("|")
    print(spltln)
    for i in spltln:
        if(i != word and i.isdigit() == False and len(i) > 1):
            return i
    return word

def main():
    word = "előtérbe állít"
    lines = readin("data.dat")
    cnt = contains(lines,word)
    if (cnt[0]):
        print(replace(lines[cnt[1]],word))
            

if __name__ == "__main__":
    main()