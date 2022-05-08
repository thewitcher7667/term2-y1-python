# previous number
# current number
# add two number "reult"
# result = previous number
#################################################################################
################################ adding the number with the sum ##################
##################################################################################
"""
while True:
    try:
     la = input("numbers only :")
     int(la)
     break
    except ValueError as e:
     print(e)
     print("Enter only numbers plz")
result = 0
for a in range(int(la)):
    curnt = a
    previus= result
    result = curnt + previus
    print("previus number is ",previus , "current number is " ,curnt ,"=",result)
"""
#####################################################################################################
########################## adding the two number ###################################################
#################################################################################################
print("input the range you want")

while True:
    try:
     la = input("numbers only :")
     int(la)
     break
    except ValueError as e:
     print(e)
     print("Enter only numbers plz")

for a in range(int(la)):
    curnt = a
    previus= curnt-1
    result = curnt + previus
    print("previus number is ",previus , "current number is " ,curnt ,"=",result)
