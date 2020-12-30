# Intercepted message
codedMessage = 'nzohfu gur rarzl ng avtug'

# We will shift by 0, shift by 1, shift by 2, ... and print the results
for counter in range(26):
    # Start with no guess
    guessedMessage = ''
    
    # Loop through each letter in the coded message
    for x in codedMessage:
        
        # If x is not a space
        if x != ' ':
            
            # Shift the letter forward by counter
            if ord(x)+counter <= 122:
                x = chr(ord(x)+counter)
                
            # Subtract 26 if we go beyond z
            else:
                x = chr(ord(x)+counter-26)
                
        # Build a guess for the message one letter at a time
        guessedMessage = guessedMessage + x  

    # Print the counter (the shift) and the message
    print(counter, guessedMessage)