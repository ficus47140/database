import hashlib

class User_unit:
  def __init__(self, password, username) -> None:
    self.password, self.username = password, username
    self.is_blocked = False

  def __str__(self):
    return f"username : {self.username}, password : {self.password}, is_block : {self.is_blocked}"

  def accesse(self, username, password):
    if username == self.username and self.password == password:
      if not self.is_blocked:
        return 0
      return -1
    return 1
  
  def block(self):
    self.is_blocked = True 
    
  def unblock(self):
    self.is_blocked = False 

  def is_block(self):
    if not self.is_blocked :
      return 0
    else:
      return 1
    
  def is_user(self, username):
    if username == self.username:
      return True
    return False
  

    
def hash_256(a):
  hash = hashlib.sha256()
  hash.update(a.encode('utf-8'))
  hash.digest()
  return hash.hexdigest()
