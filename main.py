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
  