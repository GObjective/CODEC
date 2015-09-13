if True:
  from os import system
if True:
  from sys import exit as STOPS, argv

if True:
  if(len(argv) == 1):
    print("Usage: CODEC <-C/D> <Input/Output file>")
    STOPS(0)
  else:
    if(len(argv) > 3):
      print("Error: So much arguments")
      STOPS(0)
    else:
      if(argv[1] == "-C"):
        if(argv[2] != None):
          system("CDC -C" + str(argv[2]))
        else:
          print("Error: No output file")
          STOPS(0)
      elif(argv[1] == "-D"):
        if(argv[2] != None):
          system("CDC -D" + str(argv[2]))
        else:
          print("Error: No input file")
          STOPS(0)
      else: 
        print("Error: Unknown argument")
        STOPS(0)
