from user import User_unit, hash_256
import os

class User_database:
  def __init__(self, n_row : int):
    self.n_row, self.full = n_row, False
    self.content = []

  def stock(self, content):
    if len(self.content) >= self.n_row:
      raise Exception("error : full capacity reached")
    else:
      self.content.append(content)

  def find_for_connect(self, user_name, password):
    for i in self.content:
      x = i.accesse(user_name, password)
      if x in [-1, 0]:
        return x, i
    return None
    
  def find_username(self, username):
    for i, j in zip(self.content, range(len(self.content))):
      if i.is_user(username):
        return i, j 
    return None
  
  def block_by_username(self, username):
    x = self.find_username(username)
    
    if x is not None:
      result = self.content[x[1]].is_block()
      self.content[x[1]].block()
      return result
    
  def access(self, username, password):
    x = self.find_for_connect(user_name, password)
    if x is not None:
      if x[1] == 0:
        return "acce"

user_name = input("username : ")
password = input("password : ")

user_name = hash_256(user_name)
password = hash_256(password)

user = User_unit(password, user_name)

user_database_unit = User_database(4)
user_database_unit.stock(user)

user_database_unit.block_by_username(user_name)

print(user_database_unit.find_username(user_name))

