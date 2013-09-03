    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  
#  Copyright 2013 Himanshu Mishra <himanshu.m786@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def counter():
  f = open('data.todo','r')
  count = 0
  while f.readline():

    count += 1
  return count


def info():

  # Information for the user : 
  print('''\n
    -------------------------------------------------------------
    |         \t\t ToDo List Manager :-                   |
    |                                                           |
    |           \t Select the option below :-             |
    |           \t t ) enter a task.                      |
    |           \t x ) exit.                              |
    |                                                           |
    |___________________________________________________________|
    \n''')

def main():

  
  # This while loop depends on the option that is input.
  # It run infintly and depends on user. 
  while(1):
    # Information : Providing input the user 
    info()

    # Asking for the option
    opt = input("Enter option :");

    # creating a  option for exit
    if opt == 'x':
      print("\nThank You For Using It\n")
      break

    '''
      Concept : why we are opening & closing main file varible here .(which is just creating the a new buffer for reading the file) will not
        work for reading the current inputs.
      
        So to get the current input we need close the main file i.e todoFile this is will save the on going operation. 
        We have to be caution about, when we enter the next task that should be at last.
    '''

    # For entering task
    if opt == 't':
      
      '''
      Open --> Collection --> Writing --> Close
      '''

      # file opening
      todoFile = open('data.todo','a')
      
      # collection task
      task = input("Enter Task : - ")

      # it calculate number of task already done .
      count = counter() - 2
      # writing task to file
      todoFile.write("\t\t"+str(count)+") "+task + '\n')

      # closing the file
      todoFile.close()

      # Printing the whole data.todo file
      tempBuffer = open('data.todo','r')
      print("\n\n\n"+tempBuffer.read())
      tempBuffer.close()
  return 0

if __name__ == '__main__':
  main()
