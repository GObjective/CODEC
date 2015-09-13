if True:
  if True:
    from os import system
  if True:
    from sys import argv
    argc = len(argv)  
  
if True:
  if(argc != 1 and argc < 2):
    if(argv[1] == "-C"):
      if(argv[2] != None):
        system("CDC -C " + argv[2])
      else:
        print("\033[91m" + "Error: [No input file]" + "\033[0m")
    elif(argv[1] == "-D"):
      if(argv[2] != None):
        system("CDC -D " + argv[2])
      else:
        print("\033[91m" + "Error: [No output file]" + "\033[0m") 
    else:
      print("\033[91m" + "Error: [Unknown argument]" + "\033[0m")
  else:
    print("\033[91m" + "Error: [No such argument or so much arguments]" + "\033[0m")
