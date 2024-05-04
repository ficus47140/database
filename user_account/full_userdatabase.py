from user_database import *
import os
import pickle

class full_user_database:
  def __init__(self, first_database:User_database, n_row, case):
    self.content = [first_database]
    self.n_row = n_row
    self.case = case

  def load(self):
    for i in os.listdir(self.file):
      yield pickle.load(i)

  def update(self):
    if self.content[-1].full:
      self.content.append(User_database(self.n_row))
      self.save()

  def stock(self, user, password):
    self.content[-1].stock(user, password)
    self.update()

  def connect(self, user, password):
    for i in self.load():
      x = i.find_for_connect(user, password)
      if x:
        return x
      
  def save(self):
    pickle.save(self.content[0], f"{len(os.listdir((self.case)))}.pickle")

  def block(self, username):
    for i, j in zip(self.load(), range(len(os.listdir(self.case)))):
      if i.find_username(username):
        i.block_by_username(username)
        pickle.dump(self.content[0], f"{j}.pickle")
        