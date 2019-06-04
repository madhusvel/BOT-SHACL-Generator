import random
import re

#Function for copying code from snippets to the main shape file--------------------------------------------------------------
def copyMaster(str, j):
        
        file1=open (str,"r")
        file2=open("finalSHACLShape.ttl","a+")
        #for each line in the BOT file
        for line in file1:
                file2.write(line)
        if (j ==n-1):
                file2.write(".")
        else:
                file2.write(";")
        file1.close()
        file2.close()
        print("Successfully appended",str, "to the main file.\n")

#Get User input--------------------------------------------------------------------------------------------------------------
print('Please enter all the SHACL constraints you would like to check by seperating them with space\n',
    'The options are as follows:\n 1.bot:Zone\n',  
    '2. bot:containsZone\n', 
    '3. bot:Space\n',
    '4. bot:Storey\n',
    )
selection=[int(n) for n in input('Enter your selections : ').split()]
n=len(selection)

#Create a new .ttl file for finalSHACL_shape
fileMeta=open("finalSHACLShape.ttl", "w+")
fileMeta.close()

#Copy code and append to finalSHACL_shapes.ttl file--------------------------------------------------------------------------
for i in range (0,n):
        if selection[i]==1:
                copyMaster("bot_Zone.ttl",i)
        if selection[i]==2:
                copyMaster("bot_Site.ttl",i)
        if selection[i]==3:
                copyMaster ("bot_containsZone.ttl",i)
        if selection[i]==4:
                copyMaster ("bot_Space.ttl",i)
        if selection[i]==5:
                copyMaster ("bot_Storey.ttl",i)
        #else:
        #        print("ERROR: .ttl file not found!! Please choose from the available options or update the database!!")