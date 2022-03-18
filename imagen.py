print("Elige una opción!")
menu = int(input("\n 1. Cows \n 2.Elephants  \n 3. Scorpions \n 0. Salir \n"))

while menu != 0:

 if menu == 1:
    print(""" 
    
             /)  (\
        .-._((,~~.))_.-,
         `=.   99   ,='
           / ,o~~o. \
          { { .__. } }
           ) `~~~\' (
          /`-._  _\.-\
         /         )  \
       ,-X        #   X-.
      /   \          /   \
     (     )| |  | |(     )
      \   / | |  | | \   /
       \_(.-( )--( )-.)_/
       /_,\ ) /  \ ( /._\
           /_,\  /._\
                     
   """)

 elif menu == 2:
       print(""" 
      ____
                   .---'-    \
      .-----------/           \
     /           (         ^  |   __
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | mrf
  \|, '_:::\  . ..  '_:::\ ..\).

  """)

 elif menu == 3:
    print("""
     _   _
           (.)_(.)
        _ (   _   ) _
       / \/`-----'\/ \
     __\ ( (     ) ) /__
     )   /\ \._./ /\   (
      )_/ /|\   /|\ \_(
    
    """)
    
 else:

    print("Digita una opcion correcta")

 menu = int(input("\n 1. Dog \n 2. Cows \n 3. Scorpions \n 0. Salir \n"))