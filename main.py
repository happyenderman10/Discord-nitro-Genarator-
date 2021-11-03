import random,string
import json
import os
with open('amounts.json') as json_file:
  amounts = json.load(json_file)
  last = amounts.get('amount')
os.system('color 2')
os.system('title Nitro Generator')
print("""
███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗    
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║    
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║    
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║    
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║    
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝""")
print("Waring : You wont get a lot of workings codes The chance of getting working codes is very less So you may Have luck if you get a working code")
input('')
os.system('cls')
print(f'Last Generatorated Codes : {last} ')
amount = int(input('How much nitro codes you want  to generate: '))
with open('amounts.json') as json_file:
  amounts = json.load(json_file)
  data = {'amount': f"{amount}",}
with open('amounts.json', 'w') as f:   
  json.dump(data, f, indent=4,sort_keys=True)
value = 1
while value <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    print(f'https://discord.gift/{code}')
    f = open('Nitro.txt', "a+")
    f.write(f'https://discord.gift/{code}\n')
    f.close()
    value += 1  
    
    
