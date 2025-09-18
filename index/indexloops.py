#task
# for i in range (1,51):
#     if i%3==0:
#         continue
#     print(i,end="")

#task1
# while True:
#     num=int(input("enter a number:"))
#     if num%11==0:
#         print(f"{num} is divisible by 11.exiting loop.")
#         break

#task2

# string=input("enter a string:")
# vowels='aeiouAEIOU'
# count=0
# for char in string:
#     if char in vowels:
#         count+=1
#     print(f"Number of vowels:{count}")

#task3
# num=100
# while num>=2:
#     if num%2==0:
#         print(num,end=" ")
#     num-=1    
        

# #task4
# while True:
#     password=input('enter a password')
#     if password=="admin123":
#         print("access granted!")
#         break

#task5
# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

# #task6
# count=0
# while count < 10:
#     number =int(input(f"enter number {count+1}:"))
#     if number < 0:
#         continue
#     print(f"accepted number: {number}")
#     count+=1

# #task7
# n=int(input("enter the number of odd numbers to sum:"))
# sum_odd=0
# count=0
# number=1
# while count<n:
#     sum_odd+=number
#     number+=2
#     count+=1
# print(f"sum of first {n} odd number is: {sum_odd}")

# #task8
# for num in range(2,51):
#     for i in range(2,int(num**0.5)+1):
#         if num % i==0:
#             break
#     else:
#         print(num,end=" ")    

#task9
# total=0
# while True:
#     num=int(input("enter a number(0 to stop):"))
#     if num==0:
#         break
#     total+=num
# print(f"total sum is:{total}")    




