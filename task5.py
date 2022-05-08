while True :
    enter = input("enter one Character")
    if len(enter) ==1:
        break
    else:continue
lists = ['a','b','c','d','e',f'','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','u','v','x','y','z']
listu = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','p','Q','R','S','T','X','W','Y','Z','X','J','U','v']
numb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
if enter in numb:
   print(f"the letter {enter} is NUMBER")
elif enter in lists:
 print(f"the letter {enter} is Lower case")
elif enter in listu :
 print(f"the letter {enter} is Upper case")
else :
    print(f"the letter {enter} is special character")





