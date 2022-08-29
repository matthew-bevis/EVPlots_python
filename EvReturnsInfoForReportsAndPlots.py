#this program reads in "OurDatabase.txt"  and returns
#a list ValDataBase which is in a more useful form to
#make plots and reports as well as other info useful
#for making plots and reports

from EvStudySomeListsandConstants import *

import sys #contains system commands such as exit program
import calendar #allows us to determine if we are in leap
                #year for instance

#we load up these variables to write out as plots and such
ValDataBase = [] #these will hold values needed to do plots, including titles
DataBaseMonth=""
Year = ""


DataBaseFile=open("OurDatabase.txt", "r")
TheWholeThing = DataBaseFile.readlines() #readlines discussed page 395
#This, of course, reads in the whole file into list, TheWholeThing.  Each
#element in the list is a line of the file

aline=TheWholeThing[0].split(",") # index 0 is a header line
DataBaseMonth=int(aline[1])
DataBaseYear = int(aline[3])
DaysInMonth = int(aline[7])

DataBaseFile.close()
WhereInFile = 1 #we read in the whole file, we skip the first line which
                #was a header that we already toook information from.
                #Index 1 is first real data line

ValDataBase = [] #holds values in more convenient format
while (WhereInFile < len(TheWholeThing)-1):
    if not("Dealer Num, Month, Day of Month" in TheWholeThing[WhereInFile]):
          print("EE Problem reading DataBase file, program bug")
          #this should not happen. In front of every data line
          #in the OurDatabase.txt should be a header which includes this
          #string (actually the string here is only part of  the
          #header in front of every data line, there is a bit more).
          #
          #So on this condition, we just stop whole program
          #to look for bug in our code.
          sys.exit(1)
    WhereInFile = WhereInFile + 1
    print("we are appending data line")
    print(TheWholeThing[WhereInFile])
    ValDataBase.append(TheWholeThing[WhereInFile].split(","))
    #append data line which follows header line to our ValDataBase
    WhereInFile = WhereInFile + 1

#now we get dealer info
infile=open("EV_Study_Dealer_Info.txt", "r")
#Load in information about dealers

DealerInfo = []
#We now read in dealer info,
#little error checking because
#study operations people (not dealer people)
#create this file
Done=False
line1 = infile.readline()
while (not Done):
      aDealerName = line1.strip()
      line1 = infile.readline()
      aDealerEmail = line1.strip()
      line1 = infile.readline()
      aDealerContactPerson = line1.strip()
      line1 = infile.readline()
      aDealerUrbanDesnsity = line1.strip()
      
      #now we read either a new Dealer Name or
      #or a "zz" to mean done
      line1 = infile.readline()
      if (line1.strip() == "zz"):
         Done = True

      DealerInfo.append([aDealerName,aDealerEmail,
         aDealerContactPerson, aDealerUrbanDesnsity])
      
infile.close()

def GivesUsValsToDoPlotsAndReports():
    return (DataBaseMonth, DataBaseYear, DaysInMonth,
           ValDataBase,DealerInfo)
#function returns all a plot or report program would need
#to easily get at data

#ValDataBase now has our data in a form easy for other progrmas to make
#various reports and plots from



       
      
           
           
           
           
                 
              
          
            
      
      
      
      
      
      
      
      
      



