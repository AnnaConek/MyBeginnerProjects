
"""
GUIDE: This program is meant to emulate the Character Wishing system in the video game Genshin Impact. Genshin impact is a gachapon game, meaning that you spend currency 
called "primogems" for the chance to receive either a 3-star weapon (common), a 4 star character (uncommon), or a 5-star character (rare). This game has 
"banners" which essentially mean that when you cast a wish, you have a chance at getting one special, limited-edition 5 star character that the banner specifies.

The rules for this system are as follows:
    1. 1 wish means a chance at a 3-star weapon(94.3%), 4-star character(5.1%), or 5-star character(0.6%)
    2. 90 wishes guarantees a 5-star character and 10 wishes guarantees a 4-star character
    3. 5-stars characters are either the target "banner" character (limited-edition) or a random "standard-banner" character (these are non-limited edition 5 star characters)
       The odds of getting a limited edition vs non-limited edition 5 star character is 50% (these odds are commonly dubbed "the fifty-fifty" by players)
    4. Once you get a non-limited edition 5 star, within the next 90 wishes you are guaranteed to get a limited edition character. This resets after the player
       gets the limited edition character. This is called "hard pity"
    5. In game, the odds of getting a 5-star character gradually increase as the player makes more wishes. This point supposedly begins at 76 wishes and is called "soft pity". 
    This is not explicitly released information, but rather an observation by players. I will try to incorporate this into my program as well using player collected data.
    Since this program is somewhat rudementary, the adjustments in 5-star odds will be as follows:
        0.600% for pull 1-75
        32.400% (or so) for pull 76-89
        100% for pull 90
      
"""
import random 

#universal methods
#pick a random element within an array and return it so that it can be used as a name property within a character or weapon object
def Randomize(nameslist):
    randonum = random.randint(0,len(nameslist)-1)
    name = nameslist[randonum] 
    return name

def isStandardBanner(name):
    standard = ["Diluc","Jean","Keqing","Mona","Qiqi","Tighnari","Dehya"]
    if name in standard:
        return name
    else:
        return ""

def ChooseTargetCharacter(target):
    Banners = ["Albedo","Eula","Ganyu","Hu Tao","Klee","Raiden Shogun","Tartaglia","Xiao",
               "Venti","Zhongli","Kamisato Ayaka","Yoimiya","Sangonomiya Kokomi","Arataki Itto",
               "Kamisato Ayato","Yae Miko","Shenhe","Yelan","Tighnari",
               "Cyno","Nilou","Shenhe","Yelan","Nahida","Wanderer",
               "Alhaitham","Dehya","Baizhu"]
    
    if target in Banners:
        return target
    else:
        print("not available - choosing random banner")
        return Randomize(Banners)


    
##TIME FOR THE REAL DEAL - the Wishing method(s)!!
def MakeWish():
    wishtype = int(input("1 wish or 10 wishes? Type number here: "))
    if wishtype == 1:
        return 1
    elif wishtype == 10:
        return 10
    else:
        print("not an option: please choose 1 or 10 wishes")
        return 0

    
#specific classes
#Wish class = contains user info regarding tracking wishes, currency, and closeness to pity (guaranteed fivestar)
class Wish:
    
    def __init__(self):
        self.winfiftyfifty = True
        self.pity = 90
        self.userpity = 0
        self.primogems = 14400
        self.targetchar = ""
        self.inventory = []
        
    def printpity(user):
        print(user.userpity)
    def mutatefiftyfifty(user, TF):
        user.winfiftyfifty = TF
        
    #create rarity system that adjusts as number of wishes increases
    def RaritySystem(user):
        mynum = random.randint(0,1000)
        pity = user.userpity
        odds3 = 943
        odds4 = 51
        odds5 = 6
        
        #adjust pull rate as more wishes are done by character - include guarantees
        if pity >= 0 and pity <= 75:
            odds5 = 6
        elif pity >= 76 and pity <= 89:
            odd5 = 324
        
        #return rarity of item
        if pity == user.pity:
            pity = 0
            return 5
        elif pity%10 == 0 and pity != 0:
            return 4
        elif mynum >= 0 and mynum <= odds5:
            pity = 0
            return 5
        elif mynum <= odds4:
            return 4
        else:
            return 3
            
    def fiftyfifty(user):
        
        if user.winfiftyfifty == False:
            user.winfiftyfifty == True
        elif user.winfiftyfifty == True:
            chance = random.choice([True,False])
            user.winfiftyfifty == chance
            return chance
        
    def SinglePull(user, target):
        user.targetchar = target
        user.userpity += 1
        user.primogems -= 160
        
        rarity = user.RaritySystem()
        if rarity == 3:
            weapon = ThreeStarWeapon()
            weapon.RandomWeapon()
            user.inventory.append(weapon)
            return weapon.name
        elif rarity == 4:
            Char1 = FourStar()
            Char1.RandomName4()
            user.inventory.append(Char1)
            return Char1.name
        elif rarity == 5:
            user.userpity = 0
            win = user.fiftyfifty()
            if win == True:
                Char2 = FiveStarCharacter(target)
                user.inventory.append(Char2)
                Char2.name+="*******"
                return Char2.name
            elif win != True:
                Char3 = FiveStarStandard()
                Char3.RandomName5()
                user.inventory.append(Char3)
                user.winfiftyfifty == False
                return Char3.name
                
    
        
#random 4 star character
class FourStar:    
    def __init__(self):
        self.name = ""     
        
    def RandomName4(Character):
        nameslist = ["Amber","Barbara","Beidou","Bennett","Chongyun","Diona",
                     "Fischl","Kaeya","Lisa","Ningguang","Noelle","Razor",
                     "Rosaria", "Sucrose", "Xiangling","Xingqiu","Xinyan",
                     "Yanfei","Kujou Sara","Thoma","Shikanoin Heizou","Yun Jin",
                     "Kuki Shinobu","Collei","Dori","Candace","Kaveh","Layla",
                     "Mika","Faruzan","Yaoyao",]


        
        Character.name = Randomize(nameslist)
        
# seperate 5 stars into standard banner and character banner - user chooses which character they want        
class FiveStarStandard:
    def __init__(self):
        self.name = ""
        
    def RandomName5(Character):
        nameslist = ["Diluc","Jean","Keqing","Mona","Qiqi","Tighnari","Dehya"]
        Character.name = Randomize(nameslist)
        
class FiveStarCharacter:
    def __init__(self, name):
        self.name = name
        
class ThreeStarWeapon:
    def __init__(self):
        self.name = ""
        
    def RandomWeapon(Weapon):
        weaponslist = ["Debate Club","Harbinger of Dawn","Thrilling Tales of Dragon Slayers","Bloodtainted Greatsword",
                       "Skyrider Sword","Magic Guide","Messenger","Sharpshooter's Oath","Slingshot","Raven Bow",]     
        
        Weapon.name = Randomize(weaponslist)

#main screen
class main():
    
    w1 = Wish()
    w1.printpity()
    numwishes = w1.primogems/160
    lostfifty = ""
    quit = False
    print("welcome to Genshin Impact wish simulator \nYou have " + str(numwishes) + " wishes")
    desiredchar = input("Please type the name of your target character: ")
    desiredchar = ChooseTargetCharacter(desiredchar)
    print("\nYour desired character is " + desiredchar)
    
    while True:
        if numwishes == 1:
            print("\nYou have 1 wish remaining.")
        else:
            print("\nYou have " + str(numwishes) + " wishes remaining.")
 
        pulltype = MakeWish()
        if pulltype == 1:
            tempname = w1.SinglePull(desiredchar)
            print(tempname)
            if tempname == desiredchar:
                w1.mutatefiftyfifty(True)
            else:
                w1.mutatefiftyfifty(False)
                if isStandardBanner(tempname) != "":
                    lostfifty = tempname
        elif pulltype == 10:
            numwishes = w1.primogems/160   
            if numwishes <= 9:
                print("Not enough for ten pull! Try again\n")
            else:
                for i in range(1,11):
                    tempname = w1.SinglePull(desiredchar)
                    print(tempname)
                    
                    if tempname == desiredchar:
                        w1.mutatefiftyfifty(True)
                        if isStandardBanner(tempname) != "":
                            lostfifty = tempname
                    else:
                        w1.mutatefiftyfifty(False)
                        if isStandardBanner(tempname) != "":
                            lostfifty = tempname
            
        numwishes = w1.primogems/160   
        if numwishes <= 0 :
            print("\nAll out of primogems\n")
            break
        else:
            numtoquit = input("\nPress any button to continue or type 2 to quit: ")
            if numtoquit.isdigit() and int(numtoquit) == 2:
                break
            
            
    if w1.winfiftyfifty == True:
        print("CONGRATULATIONS!! You won " + desiredchar)   
    elif w1.winfiftyfifty == False:
        if lostfifty != "":
            print("You lost the fifty-fifty to " + lostfifty + "\nbetter luck next time")
        else:
            print("No luck this time")
            
    print("Thank you for playing")


     

    
            
    
    
    
    
    
    

    