#count number of each character in the text stored in clipboard

#make sure pyperclip in installed before running
import pyperclip

def alphabetCount(recmes): #recmes=received message
    count={}
    for character in recmes.lower():
        count.setdefault(character,0) #create key for character not present already in dictionary and set value as 0
        count[character]+=1
    return count

if __name__=="__main__":
    message=pyperclip.paste()
    data=alphabetCount(message)
    print('Your text: \n'+message)
    print('\n',data)


