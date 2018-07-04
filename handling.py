try:
     f = open("ab.txt")        #by default read
     for line in f:
         print(line)

except Exception as e:
    print(e.filename)
except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print()
#except FileNotFoundError:
 #   print("File not found")            # if error occurs this will execute

#except ZeroDivisionError:
  #  print("Devided by zero")

#i=0/0
