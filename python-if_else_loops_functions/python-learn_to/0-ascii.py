#Enter a string to hide in uppercase: HIDE
#Secret message:35647890
#Original Message: HIDE
#Input "Enter a string to hide in uppercase"
normal_string = input("Enter a string to hide in uppercase: ")

secret_string = ""
#Cycle through each character in the string
for char in normal_string:

    #Store each character code in a new string
    secret_string +=str(ord(char))
#Print "Secret Message: 35647890"
print("Secret message: ", secret_string)
#Cycle through each character code 2 at a time by incfrementing by 2 each time
normal_string = ""
for i in range(0,len(secret_string)-1, 2):
    #Get 1st and 2nd for the digit number"
    char_code = secret_string[i] + secret_string[i + 1]
    #Convert the code into character into characters and add into a new string
    normal_string += chr(int(char_code))
#print original message: HIDE
print("Original message: ", normal_string)
