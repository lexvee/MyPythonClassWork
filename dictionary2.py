wordlist_filename="wordsline.txt"
#----------------------------------------
def load_words():
    
    file=open(wordlist_filename,"r")

    line=file.read()

    wordlist=str.split(line)

    return wordlist
#---------------------------------------------
wordlist=load_words()
#---------------------------------------------
def generate_dict(wordlist):

    word_dict={} #initialiazing

    for word in wordlist:

        word_dict[word]=len(word)

    return word_dict
#-----------------------------------------------
print(generate_dict(wordlist))

