
english_article="he went to the forest. he saw an elephent there, the elephant is a animal"
characters={}
articles={"definite":"",
            "indefinite":""}
for character in english_article:
    if character in characters.keys():
        characters[character]+=1
    else:
        characters[character]=1
print(characters)

list1=english_article.split(' ')
print(list1)
definite_list=[]
indefinite_list=[]
for word in list1:

    if((word == 'a' or word == 'an')):

        if(word not in indefinite_list):
            indefinite_list.append(word)

    elif(word == 'the'):

        if(word not in definite_list):
            definite_list.append(word)

articles['indefinite']=indefinite_list
articles['definite']=definite_list

print(articles)




