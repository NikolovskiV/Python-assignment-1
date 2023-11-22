# solution is a function that takes a string input_string as input and returns the deciphered string.
def solution(input_string):
   # deciphered = '' - It initializes an empty string called deciphered to store the deciphered string 
   deciphered = ''  
   # in for loop we use char.islower() to checks if it's a lowercase letter using for each character. If it is, it computes its corresponding deciphered character by subtracting its ASCII value from 219 and converting it back to a character using chr(). The ASCII value difference between the characters from 'a' to 'z' and their respective reversed characters from 'z' to 'a' is 219. The condition if char.isalpha() is used to check if the character is an alphabet letter. If it's not an alphabet letter (e.g., punctuation or other characters), it remains unchanged and is appended to the deciphered string.
   for char in input_string:
        if char.islower():
            deciphered += chr(219 - ord(char)) if char.isalpha() else char  
        else:
            deciphered += char
   return deciphered


encoded_string = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
decoded_string = solution(encoded_string)
print(decoded_string)  