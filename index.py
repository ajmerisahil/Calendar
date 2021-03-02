#importing tkinter
from tkinter import *

#import calendar
import calendar

#initializing tkinter
root=Tk()

#Setting title of our GUI
root.title("Sahil's GUI Calendar")

#year for which we want the calendar to be shown
year=2021

#storing 2020 year in myCal
myCal=calendar.calendar(year)

#showing data using Label
cal_year = Label(root , text=myCal , font="Consolas 13 bold")

#paking the label widget
cal_year.pack()

#running the program in ready state
root.mainloop()
