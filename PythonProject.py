#Lizard Person Fight, Reward System, and Weapon system implicated 
#Player Stamina System

import random, string
playerHealth = 10
playerStamina = 5
resetVal1 = playerHealth
resetVal2 = playerStamina 
inventory = {}
inventory['butterknife'] = 1
damage = inventory['butterknife']

    

def lizardPeople(spawn):
#LIZARD PERSON SPAWNS
  if (spawn == 1):
      lizAttack = random.randint(1, 2)
      health = 2
      lizType = "Small Lizard Person"
      print ("A" + " " + lizType + " " + "has appeared!")
      lizardBlock(lizType, lizAttack, health)
  elif (spawn == 2):
      lizAttack = random.randint(2, 4)
      health = 10
      lizType = "Obese Lizard Person"
      print ("A" + " " + lizType + " " + "has appeared!")
      lizardBlock(lizType, lizAttack, health) 
  elif (spawn == 3):
      lizAttack = random.randint(4, 5)
      health = 20
      lizType = "Lanky Lizard Person"
      print ("A" + " " + lizType + " " + "has appeared!")
      lizardBlock(lizType, lizAttack, health)
  elif (spawn == 4):
      lizAttack = 7
      health = 25
      lizType = "Lizard Midget Person"
      print ("A" + " " + lizType + " " + "has appeared!")
      lizardBlock(lizType, lizAttack, health)
  elif (spawn == 5):
      lizAttack = 8
      health = 35
      lizType = "Large Lizard Person"
      print ("A" + " " + lizType + " " + "has appeared!")
      lizardBlock(lizType, lizAttack, health)
  elif (spawn == 6):
      lizAttack = 1
      health = 50
      lizType = "Giant Lizard Person"
      print ("A" + " " + lizType + " " + "has appeared!")
      lizardBlock(lizType, lizAttack, health)                
  return " "
      

#Lizard Block
def lizardBlock(lizType, lizAttack, health):
  global playerHealth, playerStamina
  while(health != 0):
     attackChoice = input("Which attack will you choose?: ")
     if (attackChoice == 'la'):
      currentPlayerHealth = 0
      currentPlayerStamina = 0
      energy = 1
      currentPlayerStamina = playerStamina - energy
      playerStamina = currentPlayerStamina
      currentHealth = health - damage
      health = currentHealth
      currentPlayerHealth = playerHealth - lizAttack
      playerHealth = currentPlayerHealth
      print (lizType + " " + "took", damage, "damage!!")
      print ("You took", lizAttack, "damage!!")    
      if (currentPlayerHealth > 0):
          print (lizType + " " + "took", damage, "damage!!")
          print ("You took", lizAttack, "damage!!") 
          print ("You have", currentPlayerStamina, "stamina left!!")
          print(hud())
      if (currentPlayerHealth <= 0):
          print ("You died")
          break
      if (currentPlayerStamina <= 0):
          print ("You ran out of Stamina!")
          print ("Defenseless, the" + " " + lizType + " " + "killed you!")
          break 
      if (health <= 0 and currentPlayerHealth > 0 and currentPlayerStamina > 0): 
          print ("You have defeated the" + " " + lizType + " " + "Person!!")
          rewards1 = random.randint(1,9)   
          lootSystem1(rewards1)
          reset()
          level = input("Congrats, you have gained a level point. Select (h) for health or (s) for stamina!: ")
          levelUp(level) 
          print ("RIP" + " " + lizType)
          break
     if (attackChoice == 'ha'):
         currentPlayerHealth2 = 0
         currentPlayerStamina2 = 0
         damage2 = damage * 1.5
         energy2 = 2
         currentPlayerStamina2 = playerStamina - energy2
         playerStamina = currentPlayerStamina2
         currentHealth2 = health - damage2
         health = currentHealth2
         currentPlayerHealth2 = playerHealth - lizAttack
         playerHealth = currentPlayerHealth2
         print (lizType + " " + "took", damage2, "damage!!")
         print ("You took", lizAttack, "damage!!")
         if (currentPlayerHealth2 > 0):
             print ("You have", currentPlayerStamina2, "stamina left!!")
             print(hud())
         if (currentPlayerHealth2 <= 0):
             print ("You died")
             break
         if (currentPlayerStamina2 <= 0):
             print ("You ran out of Stamina!")
             print ("Defenseless, the" + " " + lizType + " " + "killed you!")
             break
         if (health <= 0): 
             print ("You have defeated the" + " " + lizType + " " + "Person!!")
             rewards1 = random.randint(1,9)
             lootSystem1(rewards1)
             reset()
             level = input("Congrats, you have gained a level point. Select (h) for 5 points in health or (s) for 5 points in stamina!: ")
             levelUp(level)
             print ("RIP" + " " + lizType)
             break
          
      
#ANDACONDA PERSON SPAWN(BOSS 1)
def andaconda(bossSpawn):
  global playerHealth, playerStamina
  if (bossSpawn == 10):
      print ("Oh jee the Andaconda Person has arrived!!")
      print("You have to defeat the mighty constrictor!!")
      print("ANDACONDA PERSON: 'Im a slippery snaaaaake'") 
      lizAttack = (12)
      health = (200)
      while(health != 0):
        attackChoice = input("Which attack will you choose? Choose wisely: ")
        if (attackChoice == 'la'):
          currentPlayerHealth = 0
          currentPlayerStamina = 0
          energy = 1
          currentPlayerStamina = playerStamina - energy
          playerStamina = currentPlayerStamina
          currentHealth = health - damage
          health = currentHealth
          currentPlayerHealth = playerHealth - lizAttack
          playerHealth = currentPlayerHealth
          print ("Andaconda Person took", damage, "damage!!")
          print ("ANDACONDA PERSON: 'Im a snaaaaake'") 
          print ("You took", lizAttack, "damage!!") 
          if (currentPlayerHealth > 0):
              print ("You have", currentPlayerStamina, "stamina left!!")
              print(hud())
          if (currentPlayerHealth <= 0):
              return "You died"
          if (currentPlayerStamina <= 0):
              print ("You ran out of Stamina!")
              return "Defenseless, Andaconda Person swallowed you!"  
        if (health <= 0): 
            print ("You have defeated the mighty constrictor, the Slippery Snaaaaake, ANDACONDA PERSON!!")
            reward = 1
            bossReward(reward)
            reset()
            level = input("Congrats, you have gained a level point. Select (h) for health or (s) for stamina!: ")
            levelUp(level) 
            return "RIP Andaconda Person"
        if (attackChoice == 'ha'):
          currentPlayerHealth2 = 0
          currentPlayerStamina2 = 0
          damage2 = damage * 1.5
          energy2 = 2
          currentPlayerStamina2 = playerStamina - energy2
          playerStamina = currentPlayerStamina2
          currentHealth2 = health - damage2
          health = currentHealth2
          currentPlayerHealth2 = playerHealth - lizAttack
          playerHealth = currentPlayerHealth2
          print ("Andaconda Person took", damage2, "damage!!")
          print ("ANDACONDA PERSON: 'WEEEZSNAW'") 
          print ("You took", lizAttack, "damage!!") 
          if (currentPlayerHealth2 > 0):
              print ("You have", currentPlayerStamina2, "stamina left!!")
              print(hud())
          if (currentPlayerHealth2 <= 0):
              return "Andaconda Person swallowed you!"  
          if (currentPlayerStamina2 <= 0):
              print ("You ran out of Stamina!")
              return "Defenseless, Andaconda Person swallowed you!"  
        if (health <= 0): 
            print ("You have defeated the mighty constrictor, the Slippery Snaaaaake, ANDACONDA PERSON!!!!")
            reward = 1
            bossReward(reward)
            reset()
            level = input("Congrats, you have gained a level point. Select (h) for health or (s) for stamina!: ")
            levelUp(level) 
            return "RIP Andaconda Person"

  
  

        
                
#LOOT TIER 1 FOR LIZARD PEOPLE 
def lootSystem1(rewards1):
    global inventory, damage 
    if (rewards1 == 1):
        item = "dustpan"
        damageOut = 2
        lootBlock(item, damageOut) 
    elif (rewards1 == 2):
        item = "cologne"
        damageOut = 3
        lootBlock(item, damageOut)     
    elif (rewards1 == 3):
        item = "electric toothbrush"
        damageOut = 4
        lootBlock(item, damageOut) 
    elif (rewards1  == 4):
        item = "plunger"
        damageOut = 5
        lootBlock(item, damageOut) 
    elif (rewards1 == 5):
        item = "lemon juice"
        damageOut = 6
        lootBlock(item, damageOut) 
    elif (rewards1 == 6):
        item = 'can of bear spray'
        damageOut = 7
        lootBlock(item, damageOut)
    elif (rewards1 == 7):
        item = 'bottle of windex'
        damageOut = 8
        lootBlock(item, damageOut)
    elif (rewards1 == 8):
        item = 'Ladel'
        damageOut = 10
        lootBlock(item, damageOut)
    elif (rewards1 == 9):
        item = 'G-Sword'
        damageOut = 15
        lootBlock(item, damageOut)
#Loot Block
def lootBlock(item, damageOut):
  global inventory, damage 
  print ('You found a' + ' ' + item + '!')
  answer = input("Would you like to take the" + ' ' + item + '?' + "(Damage Output:" + str(damageOut) + ')' + " " + "Select (y) to take this item: ")
  if (answer == 'y'):
    inventory = {(item): damageOut}
    damage = damageOut 
  else:
    return
  
#Boss Loot
def bossReward(reward):
    global inventory, damage 
    if (reward == 1):
        print ("You found Andaconda Person's Rubber Ducky!")
        answer = input("Would you like to take Andaconda Person's Rubber Ducky? Select (y) to take this item: ")
        if (answer == 'y'):
          inventory = {"Andaconda Person's Rubber Ducky"}
          damage = 15
        else:
          return     
#Level Up Points
def levelUp(level):
  global playerHealth, playerStamina, resetVal1, resetVal2
  if (level == 'h'):
    playerHealth += 5
    resetVal1 += 5
  elif (level == 's'):
    playerStamina += 5
    resetVal2 += 5
  else:
    return 
#Health&Stamina Reset
def reset():
  global playerHealth, playerStamina
  playerHealth = resetVal1
  playerStamina = resetVal2
  return
#HUD
def hud():
  global playerHealth, playerStamina, inventory
  return ("Health: " + str(playerHealth) + '\t' + "Stamina: " + str(playerStamina) + '\t' + "Inventory: " + str(inventory))
#OpeningInstructions
def instructions():
  print("Lizard People are attacking and its your job to stop them")
  print("Your equipped with your trusty butterknife which has spread your butter many times in the past")
  print("Your inventory is displayed as {weapon: damage output}") 
  print("You can perform two types of attacks: Light Attacks or Heavy Attacks")
  print("To perfrom a Light Attack, type in (la). For a Heavy Attack, type in (ha)")
  print("Heavy Attacks do more damage than Light Attacks but require more stamina")
  print("Running out of stamina can result in death")
  print("Have fun")
  return " " 
#OpeningMenu
def menu():
  print("Welcome to Lizard People!")
  start = input("Enter (y) to play this game, close this program to not play this game: ")
  if(start == 'y' or start == 'Y'): 
      print(instructions())
      end()
      return 'GAME OVER'
  
#Continue or end
def end():
  global inventory, spawn, playerHealth 
  if (playerHealth <= 0):
    print ('loser')
  elif(playerHealth > 0):
    spawn = 1
    print(hud()) 
    print (lizardPeople(spawn))  
    if (playerHealth > 0):
       spawn = 2 
       print(hud()) 
       print (lizardPeople(spawn))
       if (playerHealth > 0):
         spawn = 3
         print(hud())
         print (lizardPeople(spawn))
         if (playerHealth > 0):
           spawn = 4
           print(hud())
           print (lizardPeople(spawn))
           if (playerHealth > 0):
             spawn = 5
             print(hud())
             print (lizardPeople(spawn))
             if (playerHealth > 0):
               spawn = 6
               print(hud())
               print (lizardPeople(spawn))
               if (playerHealth > 0):
                  bossSpawn = 10
                  print(hud())
                  print(andaconda(bossSpawn))

      
       
              
       
       
      
      
   
  
  
  
        
    
  

    
    

spawn = 0
bossSpawn = 0 
print (menu())




