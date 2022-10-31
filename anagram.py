# write a function that identifies if two inputs are anagrams og one another, return not an anagram if not

def array():
    lst1 = []
    lst2 = []

    word_one = input(f'Enter a word')
    word_two = input(f'Enter another word')

    for x in word_one:
        lst1.append(x)

    for x in word_two:
        lst2.append(x)

    print(lst1)
    print(lst2)

    count = 0

    for x in lst1:
        for z in lst2:
            if x==z:
                count = count+1
                
    if count==len(lst1):
        print('Strings are anagrams of each other')
    else:
        print('Strings are not anagrams of each other')
    


output = array()




    

