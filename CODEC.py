if True:
  if True:
    from os import system
  if True:
    from sys import argv
    argc = len(argv)  
  
if True:
  if(argc != 0 and argc < 3):
    if(argv[0] == "-C"):
      if(argv[1] != None):
        system("CDC -C " + argv[1])
      else:
        print("\033[91m" + "Error: [No input file]" + "\033[0m")
    elif(argv[0] == "-D"):
      if(argv[1] != None):
        system("CDC -D " + argv[1])
      else:
        print("\033[91m" + "Error: [No output file]" + "\033[0m") 
    else:
      print("\033[91m" + "Error: [Unknown argument]" + "\033[0m")
  else:
    print("\033[91m" + "Error: [No such argument or so much arguments]" + "\033[0m")
