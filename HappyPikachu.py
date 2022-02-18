print('''
                                        ,'\\
          _.----.        ____         ,'  _\   ___    ___     ____
      _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
      \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
      \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
        \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
          \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
          \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
            \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
            \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
              \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                      `'                            '-._|
    ''')
print("Hello there trainer!Welcome to Viridian Forest!From here on out, you will be encountering some wild Pokemon.\n")
print("Your goal is to have a positive training experience with Pikachu!\n ")
pikachu = input("Is Pikachu here with you today? Yes or No? \n").lower()
if pikachu == "yes":
    print(''' 
       \:.             .:/
        \``._________.''/ 
         \             / 
 .--.--, / .':.   .':. \\
/__:  /  | '::' . '::' |
   / /   |`.   ._.   .'|
  / /    |.'         '.|
 /___-_-,|.\  \   /  /.|
      // |''\.;   ;,/ '|
      `==|:=         =:|
         `.          .'
           :-._____.-:
          `''       `''')
    print("Oh! I didn't notice you there, Pikachu! I hope you both are ready to encounter some wild Pokemon!\n ")
    enter = input("Are you ready to enter the Viridian Forest? Yes or No? \n").lower()
    if enter == "yes":
        print('''   ,,,                      ,,,
       {{{}}    ,,,             {{{}}    ,,,
    ,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,, 
   {{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
    ~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
    \|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
    \|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
    \|/\\|/\|/ \\|~Y~//  \|/ \|/\\|/\|/ \\|~Y~//  \|/
    \|//\|/\|/,\\|/|/|// \|/ \|//\|/\|/,\\|/|/|// \|/
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
        print("\nYou and Pikachu entered the Viridian Forest.\n"
              "BUT WHAT'S THIS?\nA Wild Charzard is blocking your way!\n")
        print('''                
              ."-,.__
                        `.     `.  ,
                      .--'  .._,'"-' `.
                    .    .'         `'
                    `.   /          ,'
                      `  '--.   ,-"'
                        `"`   |  \\
                          -. \, |
                            `--Y.'      ___.
                                \     L._, \\
                      _.,        `.   <  <\                _
                    ,' '           `, `.   | \            ( `
                  ../, `.            `  |    .\`.           \ \_
                ,' ,..  .           _.,'    ||\l            )  '".
                , ,'   \           ,'.-.`-._,'  |           .  _._`.
              ,' /      \ \        `' ' `--/   | \          / /   ..\\
            .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
            |  '          ..         `-...-"  |  `-'      / /        . `.
            | /           |L__           |    |          / /          `. `.
          , /            .   .          |    |         / /             ` `
          / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\
        / .           \ "`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
        |'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \\
        ||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
        ||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
        || '              V      / /           `   | `   ,'   ,' '.    !  `. ||
        ||/            _,-------7 '              . |  `-'    l         /    `||
        . |          ,' .-   ,' ||               | .-.        `.      .'     ||
        `'        ,'    `".'    |               |    `.        '. -.'       `'
                  /      ,'      |               |,'    \-.._,.'/'
                  .     /        .               .       \    .''
                .`.    |         `.             /         :_,'.'
                  \ `...\   _     ,'-.        .'         /_.-'
                  `-.__ `,  `'   .  _.>----''.  _  __  /
                        .'        /"'          |  "'   '_
                      /_|.-'\ ,".             '.'`__'-( \\
                        / ,"'"\,'               `/  `-.|"''')
        do = input("Pikachu is ready to attack.\nTrainer, what do you say? QUICK ATTACK or THUNDER?\n ").upper()

        if do == "QUICK ATTACK":
            print(" \nA critical hit!")
            do2 = input("Pikachu is ready to attack again.\n"
                        "Trainer, what do you say? IRON TAIL or THUNDER BOLT?\n").upper()
            if do2 == "THUNDER BOLT":
                print(" \nIt's super effective! Wild Charzard is paralyzed! It can't move!\n ")
                do3 = input(
                    "What will you do, Trainer?\n"
                    "say 'BAG' to throw a Pokeball\n"
                    "say 'ATTACK' to continue battling\n"
                    "say 'RUN' to leave this battle\n ").upper()

                if do3 == "BAG":
                    print('''      
            |@@@@|     |####|
            |@@@@|     |####|
            |@@@@|     |####|
            \@@@@|     |####/
            \@@@|      |###/
              `@@|_____|##'
                   (O)
                .-------.
              .'  * * *  `.
             :  *       *  :
             : ~  HAPPY  ~ :
             : ~ PIKACHU ~ :
             :  *       *  :
              `.  * * *  .'
                `-.....-''')
                    print("Gotcha! Charizard was caught!\nPikachu is happy and proud of your achievement!\nYou win!")
                elif do3 == "ATTACK":
                    print(
                        "Pikachu is exhausted. "
                        "Embarrassed by its lack of stamina, "
                        "Pikachu's ego is hurt and doesn't want to continue further."
                        "\nGame over.")
                elif do3 == "RUN":
                    print(
                        "Pikachu looks at you with disappointment. "
                        "Pikachu's ego is hurt and doesn't want to continue further."
                        "\nGame over.")
                else:
                    print(
                        "Hm? What was that? While you were fumbling over your decision, Charizard flew away. "
                        "Pikachu is not happy.\nGame over.")

            elif do2 == "IRON TAIL":
                print(
                    "It's not very effective. Wild Charizard scoffs and flies away.\n"
                    "Pikachu's ego is hurt and doesn't want to continue further.\nGame over.")
            else:
                print(
                    "Pikachu is confused and didn't understand your command.\n"
                    "Embarrassed at your lack of battle experience, Pikachu walks back home alone.\nGame over.")

        elif do == "THUNDER":
            print(
                " \nTHUNDER MISSES. Wild Charizard lazily looks at you with disappointment and flies away.\n"
                "Pikachu's ego is hurt and doesn't want to continue further.\nGame over.")
        else:
            print(
                "Pikachu is confused and didn't understand your command.\n"
                "Embarrassed at your lack of battle experience, Pikachu walks back home alone.\nGame over.")
    else:
        print("Come again next time!")
else:
    print("Oh. You cannot enter this area without your Pikachu. Come again next time!")


