# class Test:
#     def __init__(self):
#         print ("hello from the first class")

# Test()

class Member:
    def __init__(self, fName, lName):
        #self refers to the object that will be created based on this class
        self.memberName = fName
        self.memberLastName = lName
        
    def get_full_name(self):
        return f"{self.memberName}, {self.memberLastName}"

    # def __str__(self):
    #     return self.memberLastName

# memberName = input("Enter your name:  ")
# memberLastName = input("Enter your last name:  ")
memberName="Assma"
memberLastName="Baziz"
memberOne = Member(memberName, memberLastName)

# print(memberOne.get_full_name())
# print(Member.__str__)
# print(Member )
# print (dir(memberOne))

# print(dir(str))

print(memberOne)