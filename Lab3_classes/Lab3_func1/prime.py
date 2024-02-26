def filter_prime(list):
   prime_list = []
   for i in list:
       count = 0
       if i == 0  or i == 1:
           continue
       elif i == 2:
           prime_list.append(i)
           continue
       for j in range(2,i):
           if(i % j == 0):
               count+=1
       if(count == 0):
            prime_list.append(i)
   return prime_list
list = [1,2,3,4,5,6,7,8,9]
print(filter_prime(list))      
       