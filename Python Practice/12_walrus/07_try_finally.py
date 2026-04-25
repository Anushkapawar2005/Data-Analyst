def main():
  try:
    a = int(input("Hey, Enter a number: "))
    print(a) 
    return

  except Exception as e:
    print(e)
    return
  finally:      # finally use in mainly fun (return) - finally block is always executed even when a return stattement is encountered. 
    print("Hey I am inside of finally")

main()