list =[]
list.append(input("hi lets get some your number1"))
list.append(input("hi lets get some your number2"))
list.append(input("hi lets get some your number3"))
list.append(input("hi lets get some your number4"))
print(list)

copy_list=list.copy()
copy_list.reverse()

if (copy_list == list):
    print("its palindrome")