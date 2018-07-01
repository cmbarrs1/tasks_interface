#!/usr/bin/python3
from datetime import date, datetime, timedelta
from gtasks import Gtasks

def getnextsunday(): #get the date for the next sunday
   return (date.today()+timedelta(days=6-datetime.weekday(date.today())))

def gettoday(): #get today's date
   return date.today()

def build_tasks_list(task_list):
   global tasks
   tasks=gt.get_list(task_list)
   
def Add_task(TaskDesc, TaskDate):
   tasks.new_task(TaskDesc, TaskDate)

if __name__ == "__main__":
   gt = Gtasks()
   task_list = intput ("Enter name of list to update: ")
   build_tasks_list(task_list)
   print ("1- Add Sunday Tasks")
   print ("2- Add multiple tasks (today's date)")
   menu = input("Selection: ")
   if menu == '1':
      task_Desc=input("Task Description: ")
      Add_task(task_Desc, getnextsunday())
   elif menu == '2':
      lines = []
      while True:
         line = input("Task Description (if done just press enter):")
         if line:
            lines.append(line)
         else:
            break     
      for line in lines: 
         Add_task(line, gettoday())
   print ("Upload to Gtask Complete")      
