# print("Hello from the first line code using python, I am so excited to start  a new programming language")
#print("Hello there are you OK")
# a = 0
# while a <= 10:
#     print(a)
#     a +=1
# else :
#     print("Loop completed")

#myList=["A","B","C","D","E","F","H","I","J"]

# print(len(myList))
# print(myList)

#lenList = len(myList)
#counter = 0

#while counter < lenList :
#     print (myList[counter])
#     counter +=1
# else:
#     print("Loop completed")

# print("#" * 50)

#===================================================== Strigns methods and formating ============================================================
#myStr ='my name\'s Assma I\'m algerian'

# print (len(myStr))
# print (myStr)

# fName = input('Enter your name: ')
# fName = fName.capitalize().strip()
# print(f"your name is {fName}")
# print("your name is {}".format(fName))
# print("your name is %s" % fName)

#numTest = input('enter a number: ')

#print(numTest.zfill(3)) # 1=====>  001 

#===================================================== Lists methods ============================================================
myList = []

# for item in [1,2,3,4,5,6,7,8,9]:
#     myList.append(item)
    
# print(myList)


# I wanna write a programm that ask user to enter his favorite sites and save those sites in a list that has max length 5

# favWeb = input("Please enter your favorite web site: ").center("https://")

# myList.append(favWeb)

# print(myList)


# favWeb = "assma"
# print(favWeb.ljust(15,"#"))
# print(favWeb.center(10, "#"))

# for item in [1,2,3,4,5,6]:
#     myList.append(item)
#     print("The content of my list is : {} \n".format(myList))
#     print(f"the length of my list is : {len(myList)} \n" )

numSites = 0
# favSite = input("Let us know about your favorite web sites: ")
# while numSites < 5 :
#     favSite = input("Let us know about your favorite web sites: ").lower()
#     numSites+=1
#     myList.append(f"https://{favSite}")
# print("Thank you for sharing this experience with us. \nyour favorite sites are: {}".format(myList))

# Now I wanna write the same code using for loop 


# myList.clear()
# for item in [1,2,3,4,5]:
#     item = input("Let us know about your favorite web sites: ").lower()
#     myList.append(f"https://{item}")

# print("Thank you for sharing this experience with us. \nyour favorite sites are: {}".format(myList))

#===================================================== Password check using whilr loop ============================================================

# password="assma"
# tries = 2
# userPassword = input("enter your password: ")
# while userPassword != password  :
#     tries -=1
#     print(f"wrong password, please try again, you have still {tries} chance")
#     userPassword = input("enter your password: ")
#     if tries == 0:
#         print ("You spent all your chances")
#         break     
# else:
#     print("Congrat, your password is correct")


#===================================================== Dictionary ============================================================

# myDict = {
#     'name':'assma',
#     'country': 'Algeria',
#     'eank': 10
# }
# print(len(myDict))
# print(myDict['name'])

# languages={
#     'one':{
#         'name':'javaScript',
#         'progress': 50
#     },
#     'two':{
#         'name':'VBA',
#         'progress': 50
#     },
#     'three':{
#         'name':'c++',
#         'progress': 10
#     },
#     'four':{
#         'name':'Type Script',
#         'progress': 20
#     }
# }
# print(languages['one']['name'])
# counter = 0
# while counter < len(languages):
#     counter +=1
#     print('hello there')

# for lang in languages:
#     print(languages[lang])

# for key, value in languages.items():
#     print(f"{key} : {value}")


#===================================================== Tuples ============================================================

# myTup=(15,2,3,4,5,6,15,15,15,15,15)

# for item in myTup:
#     print(item)

# print(myTup.index(15))
# print(myTup.count(15))


#===================================================== Task from hackerrank ============================================================
# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

# currentNum =int(input("please enter a number").strip())

# if currentNum % 2 !=0 :
#     print("WEIRD")
# else:
#     if currentNum >= 2 and currentNum <= 5 :
#         print('range from 2 to 5')
#     elif currentNum >= 6 and currentNum <=20 :
#         print('range from 6 to 20')
#     elif currentNum > 20 :
#         print('range from 20')
#     else: 
#         print('out of our ranges')


#===================================================== Strings methods ============================================================

# myName = input("Please enter your name: ")

# print(myName.strip().upper())
# print(myName[:4])
# print(myName.index("S")) #case sesitive 
# print(myName.find("S")) # returns -1 if character not found
# print("hello \n my name is assma, \n I'm algerian student".splitlines())


# myName = input("Please enter your name: ")
# if myName == "":
#     print("pleease enter a valid name")
#     myName = input("Please enter your name: ")
# else:
#     print(f"Hello {myName.upper()}")


# print(myName.replace("as","AS"))

# print(myName.join("baziz"))


#===================================================== Functions ============================================================
myName = "Assma"
# def test_func():
#     print("hello there".upper())

# test_func()


# def func_with_args(name):
#     print(f"hello args {name}")

# func_with_args(myName)


# def func_with_unpacking(*people):
#     for item in people:
#         print(f"Hello {item}")
   
# func_with_unpacking("ass","fghfgh","dfgdfg","dgdfg","jklhjkl")


#===================================================== Function Recursion ============================================================

# def clear_word(word):
    
#     if len(word) == 1 :
#         return word
    
#     if word[0] == word[1]:
#         print(f"the word with condition {word}")
#         return clear_word(word[1:]) 
    
#     return clear_word(word[0]) + clear_word(word[1:])


# print(clear_word("wwwwoooooorrrrrrrlllllllldddddddddd"))



#===================================================== Function Recursion ============================================================
