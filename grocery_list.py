

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

#initialize grocery history list
#assign condition variable for while loop
grocery_history = []
stop = True

#while stop is True continue
while (stop) :
    #create new grocery item dict
    grocery_item = {}
    #gain item name for grocery item name: value
    item_name = input("Item name:\n")
    #gain item quantity for grocery item number: value
    quantity = input("Quantity purchased:\n")
    #gain item price for grocery item price: value
    cost = input("Price per item:\n")
    #update grocery item with user input values
    grocery_item.update({'name': item_name})
    grocery_item.update({'number': int(quantity)})
    grocery_item.update({'price': float(cost)})
    #append grocery item to the grocery history list 
    grocery_history.append(grocery_item)
    #prompt user to continue or finalize grocery item creation
    command_var = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
    #if the value entered is c
    if (command_var == 'c'):
      #continue to create another item
      continue
    #if the value entered is q
    elif(command_var == 'q'):
      #change boolean variable to false, stopping loop and outputting totals
      stop = False
    #if the value is other then q or c
    else:
      #return a statement asking for q or c
      print("Please enter 'c' or 'q' only")

#initialize grand total variable 
grand_total = 0.00
#loop through grocery history list
for item in grocery_history:
  #initialize and assign item total to the price * quantity
  item_total = float(item['price']) * float(item['number'])
  #add item total to the grand total
  grand_total += item_total
  #print out each item in the dictionary and their contents
  print(str(item['number']) + ' ' + item['name'] + '\t@ $%.2f ea\t$%.2f' %(item['price'], item_total))
  #reset item total to 0 for future use
  item_total = 0
#print out grand total for all items
print("Grand total: $%.2f" % grand_total)
