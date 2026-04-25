def myfun():
  print("Hello world!")



# myfun()
# print(__name__)  # In module.py o/p: __main__ beacuse this is import in main.py

# But, in main run main.py o/p: module  




if __name__ == "__main__":
    #If this code is directly executed by running the file its present in
    print("we are directly running this code")
    myfun()

    