#this program uses modules to get data  to do
#all sorts of plots.  Many programs might have
#code that does a similar thing.
#This particular program makes a plot for
#non EV sales of a chosen dealer versus  the
#average of all dealers.

from EvStudySomeListsandConstants import *
import sys #contains system commands such as exit program

from EvConstantsAboutValDatabase import *

#we load up these variables to write out as plots and such
import EvReturnsInfoForReportsAndPlots

DataBaseMonth, DataBaseYear, DaysInMonth,ValDataBase,DealerInfo = \
  EvReturnsInfoForReportsAndPlots.GivesUsValsToDoPlotsAndReports()
dealer_choice = 1

ValsFromDealer = []
ValsForAllDealers = []
XValues = []
for i in range(0,DaysInMonth):
    ValsFromDealer.append(0)
    ValsForAllDealers.append(0)
    XValues.append(i+1) #would be the day number in month

      
WhereInValDataBase = 0
while (WhereInValDataBase < len(ValDataBase)):
    ThisLine = ValDataBase[WhereInValDataBase]
    ThisDay = int(ThisLine[DayInsideDataBase])
    ThisDealer = int(ThisLine[DealerNumInsideDataBase])
    ThisBolt_EVI = int(ThisLine[CHEVY_BOLT_EVInsideDataBase])
    ThisBolt_EUV = int(ThisLine[CHEVY_BOLT_EUVInsideDataBase])
    ThisCADILLAC_LYRIQ = int(ThisLine[CADILLAC_LYRIQInsideDataBase])
    ThisGM_NON_EV = int(ThisLine[GM_NON_EVInsideDataBase])
    #some of the above might not be needed for every plot but we leave it
    #to make a useful template for creating other similar programs


    if ( ThisDealer == dealer_choice):
         ValsFromDealer[ThisDay-1] = ThisBolt_EVI + ThisBolt_EUV + ThisCADILLAC_LYRIQ

    ValsForAllDealers[ThisDay-1] = ThisBolt_EVI + ThisBolt_EUV + ThisCADILLAC_LYRIQ
    WhereInValDataBase = WhereInValDataBase + 1

NumberOfDealers = len(DealerInfo)
#o.k. now we have the data to do our plot
import matplotlib.pyplot

matplotlib.pyplot.plot(XValues,ValsFromDealer,label="Quitman")
matplotlib.pyplot.plot(XValues,ValsForAllDealers,label="All Other Dealers")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

       
      
           
           
           
           
                 
              
          
            
      
      
      
      
      
      
      
      
      



