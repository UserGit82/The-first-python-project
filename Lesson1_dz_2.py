cube_list = [x**3 for x in range (1, 1001, 2)]
print('Cоздан список кубов нечётных чисел : ',cube_list)
my_numbers_sum = 0
my_numbers_sum_list=[]
for i in range(len(cube_list)):
  my_str = str(cube_list[i])
  my_list = list(my_str)
  for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
  for i in range(len(my_list)):
      my_numbers_sum = my_numbers_sum + my_list[i]
      if my_numbers_sum % 7 == 0:
       print('Cумму чисел из нечётных кубов, делящихся на 7 : ',my_numbers_sum)