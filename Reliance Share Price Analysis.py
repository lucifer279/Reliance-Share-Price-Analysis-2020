
#Reliance Share Price Analysis

#Stock price from 2nd Mar 2020 to 30th Dec 2020

import pandas as pd
from matplotlib import pyplot as plt
import time

# Reliance Share CSV file

Data = pd.read_csv("E:\Python\Python Project Files\RELIANCE.NS.csv")


#Cleaning Data

Data_Cleaning = Data.dropna()

# print(Data_Cleaning.to_string())

#Date

Date = Data['Date']


#.......................................................................................................................

#Find maximum traded volume

Volume = Data['Volume']

VolumeMax = Data['Volume'].max()

Volume_Max = "6,52,30,035"


#To find date of maximum traded value

VolumeMaxDate = Data.loc[Data["Volume"] > 65230034]

VolumeMax_Date = '22nd April 2020'


# Mean of Traded Volume

VolumeMean = Data['Volume'].mean()

Volume_Mean = 19724155

#.......................................................................................................................

# Opening price

Open = Data['Open']


# To find maximum price of Open Price

OpenMax = Data['Open'].max()

Open_Max = 2325

# To find Mean of Open price

OpenMean = Data['Open'].mean()

Open_Mean = '1798.18'

#.......................................................................................................................

#Closing Price

Close = Data['Close']

# To find minimum price of Close price

CloseMin = Data['Close'].min()

Close_Min = 884

# To find Close Mean

CloseMean = Data['Close'].mean()

Close_Mean = '1795'

#.......................................................................................................................

# Difference between Open and Close price


Diff_Open_Close = Data['Difference Open/Close'] = Data['Open'] - Data['Close']

Diff_Open_Close_Min = Data['Difference Open/Close'].min() # -130.89


# To find Date where differnce was lowest for investment and earn short profit.

LowDate = Data.loc[Data['Difference Open/Close'] <= -130.8999020000001]

Low_Date = '10th Sept 2020'

#.......................................................................................................................


# High Share price

High = Data['High']


HighPrice = Data['High'].max()

High_Price = 2369


HighMean = Data['High'].mean()

High_Mean = '1826'

#.......................................................................................................................

#Low Share Price

Low = Data['Low']


LowPrice = Data['Low'].min()

Low_Price = 875


LowMean = Data['Low'].mean()

Low_Mean = '1767'


#.......................................................................................................................

# Difference between High and Low price

Diff = HighPrice - LowPrice

Diff_High_Low = '1494'


#Best Day for Investment in Reliance Share

LowestDate = Data.loc[Data['Low'] < 876]
HighestDate = Data.loc[Data['High'] > 2368]

Lowest_Date = "23rd Mar 2020"
Highest_Date = "16th Sept 2020"


Inv_Opp_Day = 'The best day for Investing in Reliance share was 23rd Mar 2020 price 875'

#.......................................................................................................................

# Creating Dataframe

df = pd.DataFrame({"Date": Data["Date"],"Open":Data["Open"],"Close":Data["Close"],"High":Data["High"],
                   "Low":Data["Low"]})

Describe = df.describe()

#.......................................................................................................................


#Summary


# Introduction of company and project

def Introduction():

    About = '''    Reliance Industries Limited (RIL) is an Indian multinational conglomerate company headquartered 
    in Mumbai, Maharashtra, India. Reliance owns businesses across India engaged in energy, petrochemicals,
    textiles, natural resources, retail, and telecommunications. Reliance is one of the most profitable
    companies in India,the largest publicly traded company in India by market capitalisation.\n
    On 10 September 2020, Reliance Industries became the first Indian company to cross $200 billion in market 
    capitalization.\n
    The dataset contains the data of Reliance Industries Share price from 2nd Mar 2020 to 30th Dec 2020.\n
    The main objective of this project is to analyse share prices of Reliance Industry Limited during 
    Covid 19 Pandemic.\n
    In this project we are going to analyse the dataset using Python Pandas on windows machine and this 
    project can be run on any machine support Python and Pandas.Besides pandas we also used matplotlib 
    python module for visualization of this dataset.\n
    ( Data Source – Yahoo Finance )\n\n '''

    for i in About:
        print(i,end="")
        time.sleep(0.0010)

    print(" ")
    print(" ")
    Enter = input("Press Enter to Continue: ")
    print(" ")
    ts = '.' * 80
    for i in ts:
        print(i, end="")
        time.sleep(0.0010)

# Creating Main menu

def Main_Menu():

    print("_" * 80)
    print("Main Menu")
    print("_"*80)
    print(" ")
    print("1. To see data of Reliance Share price from 2nd Mar 2020 to 30th Dec 2020\n")
    print("2. Maximum Traded Volume and Date\n")
    print("3. Opening price, Highest and Lowest\n")
    print("4. Opening and Closing price Graph\n")
    print("5. Share price, Highest and Lowest\n")
    print("6. High and Low price Graph\n")
    print("7. Best day to invest and sell Reliance Share to earn maximum profit\n")
    print("8. Best day to earn profit from Intra Day Trading\n")
    print("9. Summary\n")
    print("_" * 80)
    print(" ")

    select = int(input("Enter your Choice : "))
    print(" ")
    print(" ")

    while True:

        Go_Back = ["Y","y"]

        if select == 1:
            print("*" * 100)
            print(" ")
            print(Data_Cleaning.to_string())
            print(" ")
            print("*" * 100)
            print(" ")
            print(" ")
            break


        elif select == 2:
            print("*"*80)
            print(" ")
            print(f"Maximum Traded Volume:{Volume_Max} on Date:{VolumeMax_Date}")
            print(" ")
            print("*" * 80)
            print(" ")
            print(" ")
            break

        elif select == 3:
            print("*" * 80)
            print(" ")
            print(f"Opening price High: Rs {Open_Max} and Low: Rs {Close_Min}")
            print(" ")
            print("*" * 80)
            print(" ")
            print(" ")
            break

        elif select == 4:
            # plot() takes an optional argument 'ax' which allows you to reuse an Axis to plot multiple lines
            ax = df.plot(kind = 'line',x = 'Date',y = "Open", color = 'g')
            df.plot(kind = 'line',x = 'Date',y = "Close",ax = ax, color = 'r')
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.title("Open & Close Share price")
            plt.show()
            print(" ")
            print(" ")
            break

        elif select == 5:
            print("*" * 80)
            print(" ")
            print(f"Share price Highest:{High_Price} and Lowest:{Low_Price} ")
            print(" ")
            print("*" * 80)
            print(" ")
            print(" ")
            break

        elif select == 6:
            ax = df.plot(kind = 'line', x = 'Date', y = 'High',color = 'g')
            df.plot(kind = 'line', x = 'Date', y = 'Low',ax = ax ,color = 'r' )
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.title("High & Low Share Price")
            plt.show()
            print(" ")
            print(" ")
            break

        elif select == 7:
            print("*" * 80)
            print(" ")
            print(f"Best day to invest: {Lowest_Date}, Price: Rs {Low_Price}\n"
                  f"Best day to sell: {Highest_Date}, Price: Rs {High_Price}\n"
                  f"Profit per share: Rs {Diff_High_Low}")
            print(" ")
            print("*" * 80)
            print(" ")
            print(" ")
            break

        elif select == 8:
            print("*" * 80)
            print(" ")
            print(f"Best day to earn profit from Intraday Trading was {Low_Date}\n"
                  "Opening Price: Rs 2183 and Closing Price: Rs 2314\n"
                  "Profit per share: Rs 130 ")
            print(" ")
            print("*" * 80)
            print(" ")
            print(" ")
            break

        elif select == 9:
            print("*" * 80)
            print(" ")
            print(f"Summary\n {Describe}")
            print(" ")
            print("*" * 80)
            print(" ")
            break

    Go_Back = input("Select 'Y' for main menu or 'N' to Exit : ")
    print(" ")
    print(" ")

    if Go_Back in ("N","n"):
        print("*" * 80)
        print("Thank you")
        print("*" * 80)
    else:
        print()
        print()
        Main_Menu()

#Calling fucntion Main_Menu

Introduction()
print(" ")
print(" ")
print(" ")
Main_Menu()





