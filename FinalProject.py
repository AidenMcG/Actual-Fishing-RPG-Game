import random

print('-------------------------------------------------------------------------------------------')
print('              WELCOME TO THE FISHING TOURNY CLASSIC GAME !!!')
user_name = input('              PLEASE INPUT YOUR NAME: ')

total = 0
currency = 30
level = 1

def itemShop(currency, level):
    total = 0
    
    rod_total = 0
    reel_total = 0
    lure_total = 0

    rod_name = ''
    reel_name = ''
    lure_name = ''
    
    price_rods = {'light action(1)': 10, 'medium action(2)': 20, 'heavy action(3)': 30}
    price_reels = {'spinning(1)': 10, 'baitcaster(2)': 15, 'upgraded spinning(3)': 20, 'upgraded baitcaster(4)': 30}
    price_lures = {'worm(1)': 1, 'senko plastic worm(2)': 3, 'spinner bait(3)': 5, 'crankbait(4)': 5, 'jerkbait(5)': 7}

    price_rods = str(price_rods)
    price_rods = price_rods.replace('{', '').replace('}', '').replace("'","")
    price_reels = str(price_reels)
    price_reels = price_reels.replace('{', '').replace('}', '').replace("'","")
    price_lures = str(price_lures)
    price_lures = price_lures.replace('{', '').replace('}', '').replace("'","")
    
    item = 0
    item_type = 0
    print('-------------------------------------------------------------------------------------------')
    print('                                  ', user_name,"'s ITEM SHOP")
    print('-------------------------------------------------------------------------------------------')
    while(item != 6 and item_type != 6):
        item_type = int(input("What would you like to purchase a rod(1), reel(2), lure(3), nothing(6)? "))
        if(item_type != 6):
            if(item_type == 1):
                print('-------------------------------------------------------------------------------------------')
                print('            WELCOME TO THE FISHING ROD SECTION OF THE ITEM SHOP :) ')
                print(' THE FISHING RODS ARE LISTED BELOW WITH THEIR PRICES, AND THEIR ITEM NUMBER IN PARANTHESIS')
                print('       PLEASE SELECT THE ITEM NUMBER OF THE ROD YOU WOULD LIKE TO PURCHASE!!!')
                print('Currency: ', currency)
                print('--------------------------------------------------------------------------------------------')
                print(price_rods)
                item = int(input("Which item would you like to purchase? "))
                if(item == 1 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the light action fishing rod!')
                    print('--------------------------------------------------------------------------------------------')
                    rod_total = 10
                    rod_name = 'light action rod'
                elif(item == 2 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the medium action fishing rod!')
                    print('--------------------------------------------------------------------------------------------')
                    rod_total = 20
                    rod_name = 'medium action rod'
                elif(item == 3 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the heavy action fishing rod!')
                    print('--------------------------------------------------------------------------------------------')
                    rod_total = 30
                    rod_name = 'heavy action rod'
                else:
                    print('Would you like to continue shopping? (Y/YES) or (N/NO)')
                currency -= rod_total
                print('           ',user_name,"'s UPDATED CURRENCY AND FISHING SETUP    ")
                print('                UPDATED CURRENCY: ', currency)
                print('                UPDATED FISHING SETUP: ')
                print('                FISHING ROD: ', rod_name)
                print('                FISHING REEL: ', reel_name)
                print('                FISHING LURE/BAIT: ', lure_name)
                print('-------------------------------------------------------------------------------------------')
            elif(item_type == 2):
                print('-------------------------------------------------------------------------------------------')
                print('            WELCOME TO THE FISHING REEL SECTION OF THE ITEM SHOP :) ')
                print(' THE FISHING REELS ARE LISTED BELOW WITH THEIR PRICES, AND THEIR ITEM NUMBER IN PARANTHESIS')
                print('       PLEASE SELECT THE ITEM NUMBER OF THE REEL YOU WOULD LIKE TO PURCHASE!!!')
                print('Currency: ', currency)
                print('--------------------------------------------------------------------------------------------')
                print(price_reels)
                item = int(input("Which item would you like to purchase? "))
                if(item == 1 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the spinning reel!')
                    print('--------------------------------------------------------------------------------------------')
                    reel_total = 10
                    reel_name = 'spinning reel'
                elif(item == 2 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the baitcaster reel!')
                    print('--------------------------------------------------------------------------------------------')
                    reel_total = 15
                    reel_name = 'baitcaster reel'
                elif(item == 3 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the upgraded spinning reel!')
                    print('--------------------------------------------------------------------------------------------')
                    reel_total = 20
                    reel_name = 'upgraded spinning reel'
                elif(item == 4 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the upgraded baitcaster reel!')
                    print('--------------------------------------------------------------------------------------------')
                    reel_total = 30
                    reel_name = 'upgraded baitcaster reel'
                else:
                    print('leaving item shop')
                currency -= reel_total
                print('                UPDATED CURRENCY: ', currency)
                print('                UPDATED FISHING SETUP: ')
                print('                FISHING ROD: ', rod_name)
                print('                FISHING REEL: ', reel_name)
                print('                FISHING LURE/BAIT: ', lure_name)
                print('-------------------------------------------------------------------------------------------')
            elif(item_type == 3):
                print('-------------------------------------------------------------------------------------------')
                print('            WELCOME TO THE FISHING LURE SECTION OF THE ITEM SHOP :) ')
                print(' THE FISHING LURES ARE LISTED BELOW WITH THEIR PRICES, AND THEIR ITEM NUMBER IN PARANTHESIS')
                print('       PLEASE SELECT THE ITEM NUMBER OF THE LURE YOU WOULD LIKE TO PURCHASE!!!')
                print('Currency: ', currency)
                print('--------------------------------------------------------------------------------------------')
                print(price_lures)
                item = int(input("Which item would you like to purchase? "))
                if(item == 1 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the worm bait!')
                    print('--------------------------------------------------------------------------------------------')
                    lure_total = 1
                    lure_name = 'worm bait'
                elif(item == 2 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the senko plastic worm bait!')
                    print('--------------------------------------------------------------------------------------------')
                    lure_total = 3
                    lure_name = 'senko plastic worm bait'
                elif(item == 3 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the spinnerbait lure!')
                    print('--------------------------------------------------------------------------------------------')
                    lure_total = 5
                    lure_name = 'spinnerbait lure'
                elif(item == 4 and currency > item):
                    print('--------------------------------------------------------------------------------------------')
                    print('Congrats! You have just purchased the crankbait lure!')
                    print('--------------------------------------------------------------------------------------------')
                    lure_total = 5
                    lure_name = 'crankbait lure'
                elif(item == 5 and currency > item):
                    print('Congrats! You have just purchased the jerkbait lure!')
                    lure_total = 7
                    lure_name = 'crainkbait lure'
                else:
                    print('leaving item shop')
                currency -= lure_total
                print('                UPDATED CURRENCY: ', currency)
                print('                UPDATED FISHING SETUP: ')
                print('                FISHING ROD: ', rod_name)
                print('                FISHING REEL: ', reel_name)
                print('                FISHING LURE/BAIT: ', lure_name)
                print('-------------------------------------------------------------------------------------------')
        else:
            print('-------------------------------------------------------------------------------------------')
            print('   THANK YOU FOR SHOPPING AT THE AIDEN PRO SHOP!!! ENJOY YOUR FISHING EXPERIENCE!!!')
            print('-------------------------------------------------------------------------------------------')
            total = lure_total + reel_total + rod_total
             
            break
    if(level == 1):
        fishingLevel(total, currency)
    elif(level == 2):
        levelTwo(total, currency)
    
    
    

    
#itemShop()

#currency, rod_name, reel_name, lure_name
def fishingLevel(total, currency):
    #total = itemShop(total)
    #print(total)

 
    possible_fish = {'sunfish': 5,'bluegill': 8,'bass': 15, 'catfish': 30, 'musky': 50}
    possible_fish = str(possible_fish)
    possible_fish = possible_fish.replace('{', '').replace('}', '').replace("'","")
    print('------------------------------------------------------------------------------------------------------')
    print('WELCOME TO LEVEL ONE!!')
    print('THIS WILL BE A SIMPLE LAKE FISHING TOURNAMENT IN PENNSYLVANIA')
    print('WHILE FISHING THE POSSIBLE FISH TO CATCH ARE: ')
    print(possible_fish)
    print('AS SEEN ABOVE, THE FISH HAVE NUMBERS THAT CORRELATE TO THE MAX AMOUNT OF POINTS EARNED FROM THE CATCH')
    print('YOUR OBJECTIVE IS TO EARN 23 POINTS WITHIN 5 CASTS')
    print('GOOD LUCK', user_name,'! YOU GOT THIS!!!')
    print('-------------------------------------------------------------------------------------------------------')

    points = 0
    casts = 1

    enter = input('INPUT ANY KEY WHEN YOU ARE READY TO MAKE YOUR CASTS ')

    if(enter == ''):
        while(casts <= 5):
            cast = 0
            if(total > 0 and total <= 21):
                cast = random.randint(0, 8)
                if(cast > 0 and cast <= 5):
                    points += cast
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND SUNFISH')
                    print('Point Total', points)
                elif(cast > 5 and cast <= 8):
                    points += cast
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND BLUEGILL')
                    print('Point Total', points)
            elif(total >= 22 and total <= 38):
                cast = random.randint(9, 15)
                if(cast >= 9 and cast<= 15):
                    points += cast
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND BASS')
                    print('Point Total', points)
            elif(total > 38 and total <= 55):
                cast = random.randint(16, 30)
                if(cast >= 16 and cast <= 30):
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND CATFISH')
                    print('Point Total', points)
                    print('--------------------------------------------------------------------------------------------')
                    points += cast
            elif(total > 55 and total <= 67):
                cast = random.randint(31, 50)
            else:
                pass
            casts += 1
            
    checkWin(points, currency, level)
    #currency += 40
    #itemShop(currency)
    #levelTwo(total, currency)
    
    
def checkWin(points, currency, level):
    if(points >= 23):
        currency += 40
        print('--------------------------------------------------------------------------------------------')
        print('CONGRATS!! YOU HAVE COMPLETED LEVEL 1 OF THE FISHING TOURNY CLASSIC!!!')
        print('YOU HAVE BEEN AWARDED 40 PIECES OF CURRENCY')
        print('USE THIS CURRENCY TO REPURCHASE NEW AND BETTER ITEMS TO HELP ATTEMPT THE NEXT LEVEL')
        print('--------------------------------------------------------------------------------------------')
        print('CURRENCY: ', currency)
        level += 1
        itemShop(currency, level)
        #levelTwo(total, currency)
        
    elif(points < 23):
        currency = 30
        print('--------------------------------------------------------------------------------------------')
        print('SORRY, BUT YOU LOST THE LEVEL:(')
        print('YOU CAN RESTART THE LEVEL RIGHT NOW THOUGH')
        print('YOU WILL BE REDIRECTED TO THE ITEM SHOP WITH 30 CURRENCY')
        print('USE THIS CURRENCY TO REPURCHASE ITEMS AND ATTEMPT THE LEVEL AGAIN')
        print('GOOD LUCK', user_name, 'YOU GOT THIS')
        restart = input('Input ANY KEY WHEN YOU ARE READY TO RESTART')
        print('--------------------------------------------------------------------------------------------')
        if(restart == ''):
            itemShop(currency, level)
        
                
   
def levelTwo(total, currency):
    #print('THIS IS LEVEL 2')
    possible_fish = {'sunfish': 5,'bluegill': 8,'bass': 15, 'catfish': 30, 'musky': 50}
    possible_fish = str(possible_fish)
    possible_fish = possible_fish.replace('{', '').replace('}', '').replace("'","")
    print('------------------------------------------------------------------------------------------------------')
    print('WELCOME TO LEVEL TWO!!')
    print('THIS WILL BE A SIMPLE LAKE FISHING TOURNAMENT IN Texas')
    print('WHILE FISHING THE POSSIBLE FISH TO CATCH ARE: ')
    print(possible_fish)
    print('AS SEEN ABOVE, THE FISH HAVE NUMBERS THAT CORRELATE TO THE MAX AMOUNT OF POINTS EARNED FROM THE CATCH')
    print('YOUR OBJECTIVE IS TO EARN 75 POINTS WITHIN 5 CASTS')
    print('GOOD LUCK', user_name,'! YOU GOT THIS!!!')
    print('-------------------------------------------------------------------------------------------------------')

    points = 0
    casts = 1

    enter = input('INPUT ANY KEY WHEN YOU ARE READY TO MAKE YOUR CASTS ')

    if(enter == ''):
        while(casts <= 5):
            cast = 0
            if(total > 0 and total <= 21):
                cast = random.randint(0, 8)
                if(cast > 0 and cast <= 5):
                    points += cast
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND SUNFISH')
                    print('Point Total', points)
                elif(cast > 5 and cast <= 8):
                    points += cast
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND BLUEGILL')
                    print('Point Total', points)
            elif(total >= 22 and total <= 38):
                cast = random.randint(9, 15)
                if(cast >= 9 and cast<= 15):
                    points += cast
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND BASS')
                    print('Point Total', points)
            elif(total > 38 and total <= 55):
                cast = random.randint(16, 30)
                if(cast >= 16 and cast <= 30):
                    print('--------------------------------------------------------------------------------------------')
                    print('CAST #', casts)
                    print('CONGRATS! YOU JUST CAUGHT A', cast, 'POUND CATFISH')
                    print('Point Total', points)
                    print('--------------------------------------------------------------------------------------------')
                    points += cast
            elif(total > 55 and total <= 67):
                cast = random.randint(31, 50)
            else:
                pass
            casts += 1
    #print('currency', currency)
    #checkWin(points, currency)
    currency += 60
    #itemShop(currency)
    levelTwoCheck(points, currency, level)
    
def levelTwoCheck(points, currency, level):
    if(points >= 75):
        currency += 60
        print('--------------------------------------------------------------------------------------------')
        print('CONGRATS!! YOU HAVE COMPLETED LEVEL 2 OF THE FISHING TOURNY CLASSIC!!!')
        print('THE FIRST SEASON OF THE FISHING CLASSIC TOURNY IS OVER')
        print('SEASON TWO WILL BE RELEASED NEXT MONTH AND ALL YOUR CURRENCY WILL TRANSFER OVER')
        #print('YOU HAVE BEEN AWARDED 60 PIECES OF CURRENCY')
       # print('USE THIS CURRENCY TO REPURCHASE NEW AND BETTER ITEMS TO HELP ATTEMPT THE NEXT LEVEL')
        print('--------------------------------------------------------------------------------------------')
        print('CURRENCY: ', currency)
        print('--------------------------------------------------------------------------------------------')
        print('THANK YOU FOR PLAYING THE FISHING CLASSIC TOURNY!! STAY TUNED FOR MORE TOURNAMENTS IN THE FUTURE!')
        #level += 1
        #itemShop(currency, level)
        #levelTwo(total, currency)
        
    elif(points < 75):
        currency = 30
        print('--------------------------------------------------------------------------------------------')
        print('SORRY, BUT YOU LOST THE LEVEL:(')
        print('YOU CAN RESTART THE LEVEL RIGHT NOW THOUGH')
        print('YOU WILL BE REDIRECTED TO THE ITEM SHOP WITH 30 CURRENCY')
        print('USE THIS CURRENCY TO REPURCHASE ITEMS AND ATTEMPT THE LEVEL AGAIN')
        print('YOU WILL HAVE TO START BACK AT LEVEL 1')
        print('GOOD LUCK', user_name, 'YOU GOT THIS')
        restart = input('Input ANY KEY WHEN YOU ARE READY TO RESTART')
        print('--------------------------------------------------------------------------------------------')
        if(restart == ''):
            itemShop(currency, level)


itemShop(currency, level)
