wordlist_filename="words.txt"
#----------------------------------------
def load_words():
    
    file=open(wordlist_filename,"r")

    line=file.read()

    wordlist=str.split(line)

    return wordlist
#---------------------------------------------
wordlist=load_words()
#---------------------------------------------
def dict_group(wordlist):

    word_group_dict={} #initialiazing

    for word in wordlist:

        word_key = str(len(word))+"letters"

        if word_key in word_group_dict.keys():

            word_group_dict[word_key].append(word)

        else:

            new_list=[word]
                       
            word_group_dict[word_key]=new_list

    return word_group_dict
#-----------------------------------------------
print(dict_group(wordlist)['3letters'])

