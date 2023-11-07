import sys
import gameprocess


print('(N)ew Game')
print('(L)oad Game')
print('(E)xit')

while True:

      answer = input()

      if answer == 'N': main_game()
      elif answer == 'L': load_game()
      elif answer == 'E': print('Exiting...'); sys.exit()
      else: print('Invalid option. Try again.')



