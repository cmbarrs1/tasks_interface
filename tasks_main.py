#!/usr/bin/python3
from datetime import date, datetime, timedelta
from gtasks import Gtasks

def getnextsunday(): #get the date for the next sunday
   return (date.today()+timedelta(days=6-datetime.weekday(date.today())))

def gettoday(): #get today's date
   return date.today()

def build_tasks_list(task_list):
   global tasks  #needs to be global so tasks can be used outside of def
   tasks=gt.get_list(task_list)
   
def Add_task(TaskDesc, TaskDate):  #add new task to selected list
   tasks.new_task(TaskDesc, TaskDate)

if __name__ == "__main__":
   gt = Gtasks()
   task_list = input ("Enter name of list to update: ") #Needs to be existing task list at this time.
   build_tasks_list(task_list)
   print ("1- Add Individual Sunday Tasks")
   print ("2- Add multiple tasks (today's date)")
   print ("3- Add Standard Sunday Task List")
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
   elif menu == '3':
      Add_task('Change Robin Sheets', getnextsunday())
      Add_task('Change Teddy Sheets', getnextsunday())
      Add_task('Change Master Bed Sheets', getnextsuday())
      Add_task('Vacuum Upstairs Hallway / Bedrooms', getnextsunday())
      Add_task('Vacuum Stairs', getnextsunday())
   print ("Upload to Gtask Complete")      
