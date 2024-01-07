#user-defined exceptions

class custom1(Exception):  #custom1 class inherits from the Exception class
  def __init__(self,mesg):  #constructor method with 2 parameters: self->a reference to the instance being created, msg->a string that represents te error message
    self.mesg=mesg
    super().__init__(mesg)

try:
  raise custom1("This is a message...") #this is the custom error message
except custom1 as c:
  print(f"Caugt a custom error: {c}")

#user-defined exc. with specific conditions
class valTooSmall(Exception):
  def __init__(self,val):
    self.val=val
    super().__init__(f"value {val}: is too small, it should be greater than 10")

try:
  user_input=int(input("Enter a nr greater than 10:"))
  if user_input<=10:
    raise valTooSmall(user_input) #if smaller than 10,it calls valTooSmall exception
  else:
    print(f"The number is {user_input}")
except valTooSmall as v:
  print(f"Error at {v}")
except ValueError:
  print("Invalid input. Please enter an integer.")

#multiple user-defined exceptions