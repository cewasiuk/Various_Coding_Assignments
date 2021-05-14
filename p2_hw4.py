#!/usr/bin/env python3
  
#
#Read csv file, store info in a list of python dictionaries, prompts user for a key, return values and allows user to continue
#to select keys until done
#
#25April20

csv = open('/home/pi/cewasiuk_hw/cewasiuk_hw4/test.csv', 'r')
read_csv = csv.readlines()


dict_list = []
for i in range(len(read_csv)):
	stripped = read_csv[i].rstrip('\n')
	split = stripped.split(',')
	freshdict = {'last':split[0], 'first':split[1], 'color':split[2], 'food':split[3], 'subject':split[4], 'physicist':split[5]}
	dict_list.append(freshdict)

while True:
     print('color, food, subject, physicist')
     key = input('Choose keyword, if finished please type done: ')
     c = [] 
     if key  == 'done':
         break

     for i in range(len(dict_list)):
         d = '%s, %s: %s' %(dict_list[i]['last'], dict_list[i]['first'], dict_list[i][key])
         c.append(d)
     c.sort()

     for i in range(len(c)):
         print(c[i]) 


