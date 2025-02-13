def main():
    with open("./books/frankenstein.txt") as f :
        file_contains = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(str(len(file_contains.split()))+" words were found in the document")
        print("\n")
        collection = {}
        for x in file_contains.split() :
            for y in x :
                if y.lower() in collection :
                    collection[y.lower()] += 1
                else :
                    collection[y.lower()] = 1 
        # print(collection)
        # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in collection :
            if(ord(i)>=97 and ord(i)<=122) :
                print("The '"+str(i)+"' character was found "+str(collection[i])+" times")
if __name__ == "__main__":

    main()
