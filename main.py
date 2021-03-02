#Day 1 - 1h
#a="This is test"
#string, integer, float
#a = "info"
#b = "test"
#c = a
#a = b
#b = c
#b,a=a,b
#print(a)
#print(b)
#test
#info
#a = 5
# b = 10
# print(a * b)
#*,+,-,/,%
#5%2=1 give the rest after dividing though in this case 2
#user_input = input("Please input your name")
#user_input1 = input("Please input a first numbers  ")
#user_input2 = input("Please input a second numbers to multi ")
#user_input1 = int(user_input1)
#user_input2 = int(user_input2)
#print("the answer of calculation is =")
#print(user_input1 * user_input2)
#string concatenation -> improvement
#user_input1 = int(input("Please input a first numbers  "))
#user_input2 = int(input("Please input a second numbers to multi "))
#print("The result of calculation is",user_input1*user_input2," which is right")
#print(f"The result of calculation is {user_input1*user_input2} which is right {user_input1}")

# Day 2 - 1h
#list,tuple,set
l=[]    #list can be edited and changed
t=()    #tuple is fixed and cannot be changed
s={}    #set cannot be the same value/ text
#list = ["user1", "user2","user3"]   # different inputs possibnle ( 5  ,100 , "text", "user_input") -> as variable
#list[1]
#list[1:3]
#list.pop(4)           # .pop will remove a defined "position" from the list
#list.append("Jay")    # .append (add someething to a list) is a fixed command (cannot be changed)
#list[2]="new_value"
#api_passed_value = "user1"
#api_passed_value = input("please type in your name ")   # this usually would come from Frontend
#if api_passed_value in list:
#    print("User is logged in")
#else:
 #   print("user does not exist")
#print(list)
#t=(1,2,3)
#t.append("jay")    # not possible to make .append or .pop
#s={int}    # only int or only strg or only floats --> e.g. type mobile number on a web page - exclude other inputs

#b=5
#a="5"
#print(a==b)
#==,!=,<,>,<=,>=,is  Boolean   # is: compares two variables/ lists with not only the valus but as well the memory address
#a=[1,2]
##b=[1,2]
#print(a is b)

#create users input, check if day is saturday, if true return "its weekend start", if not and day is sunday return "end of weekend, if no and day mon - fri, return its weekday
#a = "Monday"
#b = "Tuesday"
#c = "Wednesday"
#d = "Thursday"
#e = "Friday"
#f = "Saturday"
#g = "Sunday"
#working_days=[a,b,c,d,e]   # with a list necessary to think about capital letters or lower letters for the placed varables
#input_user = input("please type the day of today: " )
#if inpur_user === "Monday"
#if input_user == f:
#    print("its weekend start")
#elif input_user == g:
#    print("end of weekend")
#elif input_user in working_days:    # alos possible command: not in
#    print("working days")
#else:
#    print("invalid input")

# change the sequence 1st compare with sunday and than compare with saturday and then put the rest in command else

#if condition:
 #   do this
#elif condition:
#    do this
#else:
#    do this

#day 3 - 1,5h
#list comprehension
#a=[2,3,4]
#b=[n*2 for n in a]
#print(b)

# while 1==1:
#     gerade = []
#    ungerade = []
#     if the above liste are inside the while command, the code will always starts with a empty list - therefore to fill the list
#     it has to be outside the while command
#     input_user = int(input("please type a number: "))
#     5%2=1
#     4%2=0
#
#     if input_user%2==1:
#        ungerade.append(input_user)
#     elif input_user%2==0:
#        gerade.append(input_user)
    #print("this is gerade: ",gerade)
    #print("this is ungerade: ",ungerade)

#while loop
#while (condition):
#while 1==1:
#    print("My name is jaz")

#do while:
#    printt()
#(conditon)

#for loop
#list "days" of 20 element
#for day in days:
#    print(day)
#days=["Monday","Tuesday","wednesday"]
#for day in days:
#    print(day)

#cooljrb9@gmail.com test
#CoOljRb9@gmail.com
#a=["b","c","d"]
#for r in a:
#    print("This is first element",r)


# username_random_case = ["aBc@gmx.de","Bsa@gmx.de","fVv@gmx.de"]
# username_lower_case = []
# for each_user_email in username_random_case:      # each_user_email is a free defined wording, only logical info for the coder
#     lower_case_email = each_user_email.lower()
#     username_lower_case.append(lower_case_email)   # add with .append to the lower case list
# input_user = input("Please type your mail adress: ")
# input_user = input_user.lower()                       # variable will change from randon style to lower letters
# for input_user_lower_email in username_lower_case:
#     if input_user == input_user_lower_email:
#         print("good to start")
#     else:
#         print("email not correct!")
#     break
    # list with 3 user ID and add list with 3 passwords / first user fits to first PW / for loop and if loop to be used
    # input user name -> new input with pW and info if something is typed in wrong


# Homework: from day 3

usermail_random_case = ["aBc@gmx.de","Bsa@gmx.de","fVv@gmx.de"]
usermail_lower_case = []
for each_user_email in usermail_random_case:
    lower_case_email = each_user_email.lower()
    usermail_lower_case.append(lower_case_email)

userpassword_list = ["test11","test22","test33"]

input_user = input("Please type your mail adress for login: ")
input_user_mail = input_user.lower()                       # variable will change from randon style to lower letters
for input_user_mail_lower_email in usermail_lower_case:
    if input_user_mail == input_user_mail_lower_email:
        print("Type in your password")
    else:
        print("email not correct!")
    break



#day 4:  1h - Git / GitHub install etc.
#day 5:



