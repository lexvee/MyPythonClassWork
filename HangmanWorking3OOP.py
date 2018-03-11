import random

class FileAction():
    def __init__(self,filename):
        self.filename=filename
        return None

    def _loadwords(self):
        wordfile=Open(self.filename,'r')
        content=wordfile.read()
        return wordlist

    def pickword(self):
        word=random.choice(self._loadwords())
        return word

class PickWord(FileAction):
    pass
    
file_action=FileAction('word.txt")

print(file_action.pickword())
                           
