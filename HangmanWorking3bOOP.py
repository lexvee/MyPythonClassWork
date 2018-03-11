import random

class FileAction():

    def _loadwords(filename):
        wordfile = open(filename,'r')
        content=wordfile.read()
        wordlist=content.split()
        return wordlist

    @classmethod
    def pickword(self,filename):
        wordlist = self._loadwords(filename)
        word=random.choice(wordlist)
        return word

                           
