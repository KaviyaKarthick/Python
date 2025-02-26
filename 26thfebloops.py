#while

# a=10
# while a>=0:
#     print(a)
#     a=a-2
# print("End")

# new=input("who are you?")
# while new != "kaviya":
#     print("hi",new)
#     break
# print("not correct")

#definite loops (For)

# family =["kaviya", "karthick","kavinilaa"]
# for family in  family:
#     print("Hi", family)
# print("done")

# a=1
# for b in [1, 2, 23, 45, 54]:
#  print (a, b)
#  a=b+a 
# print ("end")

# for a in [2,4,54,23,151,100]:
#     if a >=100:
#         print("grater than 100", a)
# print("end")

# a = False
# for b in [2, 4, 5, 6, 9, 10]:
#     if b > 5:
#         a = True
#     print(b,a)
# print ("end")
    
a= None
for b in [23, 42, 12, 3, 45, 2]:
    if a is None:
        a=b
    elif a>b:
        a=b

print(a)
