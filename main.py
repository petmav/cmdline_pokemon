import sys
import gameprocess

print('(N)ew Game')
print('(L)oad Game')
print('(E)xit')

while True:

      answer = input()
      
      match answer.upper():
            case 'N':
                  print("maingame")
            case 'L':
                  print("loadgame")
            case 'E':
                  print("exit")
                  sys.exit()
            case _:
                  print("invalid")
       
