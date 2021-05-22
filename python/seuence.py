# a_list=[4,2,3,8,12,15]
# i=0
# a=0
# n=[]
# while i<15:
#     a=a+1
#     if a not in n:
#         n.append(a)
#     i=i+1
# print(n)

# mark=[23,4,5,89,90,56,80]
# i=0
# total=0
# while i<len(mark):
#     total=total+mark[i]
#     i=i+1
# print("total marks="+str(total))

# student=["risabh","madhurima","rahul","abhisekh","faizal","muskan"]
# marks=[10,20,56,45,36,20]
# i=0
# while i<len(student):
#     print(student[i],marks[i])
#     i=i+1

# list=[5,8,7,15,25,35]
# i=0
# a=[]
# y=[]
# while i<len(list):
#     b=list[i]
#     if b%5==0:
#         a.append(b)
#     else:
#         y.append(b)
#     i=i+1
# print("divisible:",a,"not divisible:",y)

# marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# sum=0
# count=0
# while i<len(marks):
#     num=marks[i]
#     a=num[0]+num[1]+num[2]+num[3]+num[4]
#     a=num[0]+num[1]+num[2]+num[3]+num[4]
#     a=num[0]+num[1]+num[2]+num[3]+num[4]
#     count=count+1
#     sum=sum+a
#     i=i+1
# print("total marks=",sum,"count:",count)

# num=[2,5,9,20,25,4,3]
# i=0
# a=[]
# b=[]
# while i<len(num):
#     c=num[i]
#     if c%2==0:
#         a.append(c)
#     else:
#         b.append(c)
#     i=i+1
# print("even num:",a,"odd num:",b)

# a=["pooja","sona","jayshri","rathod"]
# i=0
# while i<len(a):
#         j=0
#         count=0
#         while j<len(a[i]):
#                 count=count+1
#                 j=j+1
#         if count%2==0:
#                 print(a[i],"even")
#         else:
#                 print(a[i],"odd")
        
#         i=i+1

# a=[1,2,3]
# multiple_list=[a*2 not in a]
# print(multiple_list)

# a=[1,2,3]
# multiple_list=[a*2 in a]
# print(multiple_list)


# my_list=[1,2,3,4,5]
# my_new_list=[i*5 for i in my_list]
# print(my_new_list)

# a=[2,3,4,5,6,7]
# b=[3,5,4,1,6,3]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]+b[i]
#     i=i+1
# print(sum)

# num=[10,20,130,40,50,70]
# a=num[0]
# b=num[0]
# i=0
# while i<len(num):
#     if a>num[i]:
#         a=num[i]
#     if b<num[i]:
#         b=num[i]
#     i=i+1
# print(a)
# print(b)

# mainstr="the quick brown fox jumped over the lazy dog.the dog slept over the verandah"
# a=mainstr.split()
# i=0
# while i<len(mainstr):
#     if "over"in a:
#         a.remove("over")  
#     if "on"not in a:
#         a.insert(5,"on")
#         a.insert(12,"on")
#     i=i+1
# print(a)

# elements=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# even=0
# odd=0
# while i<len(elements):
#     if elements[i]%2==0:
#         even=even+elements[i]
#         average_k=even/len(elements)
#     else:
#         odd=odd+elements[i]
#         average_p=odd/len(elements)
#     i=i+1
# print(average_k,"average of even number")
# print(average_p,"average of odd numbers")

# kitna_paisa_hai=[3000.600000,324990909,30000,5600000,690909090,31010101,532010,510,4100]
# i=0
# count1=0
# count2=0
# count3=0
# while i<len(kitna_paisa_hai):
#     if kitna_paisa_hai[i]>=10000000:
#         count1=count1+1
#     elif kitna_paisa_hai[i]>=100000 and kitna_paisa_hai[i]<=9999999:
#         count2=count2+1
#     else:
#         count3=count3+1
#     i=i+1
# print(count1,"caropati hai")
# print(count2,"lakhpati hai")
# print(count3,"dilwale hai")

# num=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# i=0
# k=[]
# while i<len(num):
#     n=num[i]
#     if n not in k:
#         k.append(n)
#     i=i+1
# print(k)

# char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
# i=0
# a=[]
# while i<len(char_list):
#     j=0
#     count=0
#     b=[]
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count+=1
#         j+=1
#     b.append(char_list[i])
#     b.append(count)
#     if b not in a:
#         a.append(b)
#     i=i+1
# print(a)

 
# question_list = [
#     "1.How many continents are there?",              # pehla question
#     "2.What is the capital of India?",            # doosra question
#     "3.NG mei kaun se course padhaya jaata hai?"    # teesra question
# ]

# options_list = [
#     #pehle question ke liye options
#     ["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#     #second question ke liye options
#     ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#     #third question ke liye options
#     ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
# ]
# solution_list = [3, 4, 1]



# answer_list=[["(4),eight","(3),seven"],["(1),Chandigarh","(4),Delhi"],
# ["(1),software engineering","(2),counseling"]]
# print("welcome to the KBC")



# i=0
# sum=0
# count=0
# while i<len(question_list):
#     print(question_list[i])
#     j=0
#     a=i
#     while j<len(options_list[i]):
#         print(options_list[a][j])
#         j=j+1
#     lifeline=input("if u want 5050 lifeline or not")
#     if lifeline=="yes":
#         print("5050 lifeline")
        # if count<1:
        #     print(answer_list[i])
        #     ansrwe_1=int(input("enter your answer"))
        #     if ansrwe_1==solution_list[i]:
        #         sum=sum+10000
        #         print("congratulation your answer is correct,you won",sum,"Rs")
        #     else:
        #         print("sorry your answer is wrong,you will not play,you won",sum,"Rs")
        #         break
        #     count=count+1
        # else:
        #     print("you can't use lifeline")
        #     answer_2=int(input("enter your answer"))
        #     if answer_2==solution_list[i]:
        #         sum=sum+10000
#                 print("congratulation your answer is correct,you won",sum,"Rs")
#             else:
#                 print("sorry your answer is wrong,you will not play,you won",sum,"Rs")
#                 break
#     else:
#         pass
#         answer_3=int(input("enter your answer"))
#         if answer_3==solution_list[i]:
#             sum=sum+10000
#             print("congratulation your answer is correct,you won",sum,"Rs")
#         else:
#             print("sorry your answer is wrong,you will not play,you won",sum,"Rs")
#             break
#     i=i+1
# print("thanks for being the part of KBC game")

# num=int(input("enter the num"))
# b=str(num)
# lenth=len(b)
# k=lenth-1
# i=0
# while i<len(b):
#     code=int(b[i])
#     n=(code)*10**k
#     if i==0:
#         print("'",num,end=" ")
#     else:
#         print(n,end=" ")
#     if i!=len(b)-1:
#         print("+",end=" ")
#     i+=1
#     k=k-1
# print("'")

# binary_numbers=[1,0,0,1,1,0,1,1,0]
# g=[]
# sum=0
# decimal=0
# i=0
# lenth=len(binary_numbers)
# while i<lenth:
#     w=lenth-i-1
#     r=binary_numbers[w]
#     g.append(r)
#     decimal=g[i]*2**i
#     sum=sum+decimal
#     i=i+1
# print(sum)

# elements=[23,14,56,12,19,9,15,25,31,42,43]
# count=0
# even=0
# odd=0
# sum=0
# even_sum=0
# odd_sum=0
# i=0
# while i<len(elements):
#     count=count+1
#     sum=sum+elements[i]
#     average=sum/len(elements)
#     if elements[i]%2==0:
#         even=even+1
#         even_sum=even_sum+elements[i]
#         average1=even_sum/len(elements)
#     else:
#         odd=odd+1
#         odd_sum=odd_sum+elements[i]
#         average_0=odd_sum/len(elements)
#     i=i+1
# print(count,sum,average)
# print(even,even_sum,average1)
# print(odd,odd_sum,average_0)

# marks=[[78,76,94,86,88],[91,71,98,65],[95,45,78],[87,67,49,68,88]]
# i=0
# while i<len(marks):
#     k=0
#     sum=0
#     avarege=0
#     while k<len(marks[i]):
#         num=(marks[i][k])
#         sum=sum+num
#         average=sum/len(marks[i])
#         k=k+1
#         j=int(average)
#     print(j)
#     i=i+1


# list=[1,2,3,[4,5,7],8,1]
# i=0
# sum=0
# count=0
# while i<len(list):
#         if i==3:
#             j=0
#             s=0
#             while j<len(list[i]):
#                     s=s+list[i][j]
#                     j=j+1
#         else:
#             sum=sum+list[i]
#         i=i+1
# print(sum+s)        

# a=[[1,3,5],[5,7,8],[8,6,4]]
# i=0
# sum=0
# while i<len(a):
#         j=0
#         s=0
#         while j<len()

# i=0
# sum=0
# while i<len(a):
# a=[1,2,3,[4,5],6,7,[8,9],1,2,3,[4,5],[7,5,4,7]]
        #  if type(a[i])==type(a):
#                 j=0
#                 while j<len(a[i]):
#                       sum=sum+a[i][j]
#                       j=j+1
#         else:
#             sum=sum+a[i]
#         i=i+1
# print(sum)
                 
# num=int(input("enter the number"))
# list=[1,2,3,4,5,6,7,8,9,10,11,12,15]
# k=[]
# i=0
# while i<len(list)-num :
#         k.append(list[i])
#         i+=1
# j=1
# while j<=num :
#         k.append(list[-j])
#         j+=1
# print(k)

# a=[3,9,8,[5,10],[7,22,[33,42]]]
# print (a[3])
# print(a[4][0])
# print(a[4][2][0])
















