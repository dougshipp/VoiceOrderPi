# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 01:00:14 2017

@author: Dshippp
"""

def Main():
    keyword=input('What would you like to eat: ')
    if ((keyword)==("Dominos")):
        food=input("Do you want pizza or a sandwich?")
        if (food=='pizza' or 'Pizza'):
            pizzaDict={"1":'ExtravganZZa',"2":'MeatZZa',"3":'Philly Cheese Steak',"4":'Pacific Veggie',"5":'Honolulu Hawaiian',"6":'Deluxe',"7":'Cali Chicken Bacon Ranch',"8":'Buffalo Chicken',"9":'Ultimate Pepperoni',"10":'Memphis BBQ Chicken',"11":'Wisconsin 6 Cheese',"12":'Spinach & Feta'}
            pizzaNum=input('What number pizza do you want: ')
            response1=pizzaDict.get(pizzaNum)
            yno=input("You want the "+response1+"?")
            if (yno=='yes' or "YES"):
                print()
        else:   
            sandwichDict={"1":'Italian Sausage & Peppers',"2":'Buffalo Chicken',"3":'Chicken Habanero',"4":'Mediterranean Veggie',"5":'Chicken Bacon Ranch',"6":'Italian',"7":'Chicken Parm'}
            sandwhichNum=input('What number sandwich do you want? ')
            print("okay")
#            response2=sandwichDict.get(sandwhichNum)
#            print("You want the "+response2+"?")
    
    
    if (keyword=='Conrads'):
        Conrads()

        
# def Dominos():

def Conrads():
    conrads=input('Would you like an Original Wrap, a Chicken Tender Wrap, or a Giant Wrap?')
    if (conrads=='original' or 'original Wrap '):
        originalDict={'1':'NUMBER ONE','2':'HRK NASTY','3':'THE J.F.K.','4':'T-TOT SPECIAL','5':'SWEET THAI','6':'SPICY CHICKEN','7':'BEST ONE','8':"CONRAD'S CLUB",'9':'C-BURGER','10':'VEGGIE DELIGHT','11':'SKILLS MILLS','12':'CHEESE STEAK','13':'BBQ STEAK','14':'LUCHADOR'}
        originalNum=input('What number wrap do you want? ')
        response=originalDict.get(originalNum)
        yno=input("You want the "+response+"?")
        if (yno=='yes' or "yes"):
            print()
            
    elif (conrads=='chicken Tender' or 'chicken'):
        chickenDict={'1':'O.G.C.T.','2':'BUFFALO RIDER','3':'HONEY MUSTARD & BBQ','4':'HAWAIIAN REED','5':'CORDON LUKE','6':'CHICKEN BACON SWISS','7':'CHICKEN PARMESAN','8':'DON VITO'}
        chickenNum=input('What number wrap do you want? ')
        response=chickenDict.get(chickenNum)
        yno=input("You want the "+response+"?")
        if (yno=='yes' or "yes"):
            print()
            
    elif(conrads=='giant Wrap' or 'giant'):
        giantDict={'1':'THE BIG ONE','2':'T-TOT + CHICKEN','3':'MEGA TENDER','4':'JEMALTY','5':'THE D.W.B.!!','6':'BIG BREAKFAST'}
        giantNum=input('What number wrap do you want? ')
        response=giantDict.get(giantNum)
        yno=input("You want the "+response+"?")
        if (yno=='yes' or "yes"):
            print()

    


