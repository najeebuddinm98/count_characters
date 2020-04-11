#count number of each alphabet in any entered data

def alphabetCount(recmes): #recmes=received message
    count={}
    for character in recmes.lower():
        count.setdefault(character,0) #create key for character not present already in dictionary and set value as 0
        
        count[character]+=1
    return count

if __name__=="__main__":
    message=input('Enter your text (press enter to proceed): \n')
    data=alphabetCount(message)
    print('\n',data)


