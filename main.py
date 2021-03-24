###solution to exercise 92 from ben stephenson's "the python workbook".

def is_prime(num):
  if num == 1:
    return True
  elif num == 2:
    return True   
  else:
    result = True
    for i in range(2, num // 2 + 1):
      if not (num % i):
        result = False
        break
    return result

num = int(input('Enter an integer: '))
if is_prime(num):
  print('That is prime.')
else:
  print('That is not prime.')
