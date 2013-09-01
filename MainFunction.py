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



def main():

  print('''
    \t\t ToDo List Manager :- 

\t         Select the option below :-
\t         t ) enter a task.
\t         x ) exit.

    ''')
  # This while loop depends on the option that is input.
  # It run infintly and depends on user. 
  while(1):
    opt = input("\t\t Enter option :");
    if opt == 'x':
      break


  return 0

if __name__ == '__main__':
  main()
