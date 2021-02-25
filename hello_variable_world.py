#Jacqueline Pezan

#Collects Users Input for Names
myname = input("My name is Jackie")
nbrname = input("What is Your Name")

#Collects Users Input for Coding
mycoding = int(input("How Many Months Have I Been Coding?"))
nbrcoding = int(input( f"How Many Months Has {nbrname} Been Coding?"))

# #C ollects Users Input
# # non-empty objects are truth-y
trueOrFalse = bool(input("Is the answer truthy?"))

#I've Been Coding
print( f"{myname} has been coding {myname} months")

#Neighbor Has Been Coding
print( f"{nbrname} has been coding {nbrcoding} months")