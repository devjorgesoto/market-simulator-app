import time

#FIXED SEQUENCE

fixed_sequence = []

for x in range (1,101):
        time.sleep(.01)
        fixed_sequence.append(x)



def last_sequence(sequence_length:int):

    # Function that creates a new sequence from an existent sequence.
    # This new sequence get the last x number of items from that existent sequence.
    # x defines how many items you want to extract.

    sl = sequence_length-1

    last_sequence = []

    for x in fixed_sequence:
            
            if x >= len(fixed_sequence)-sl:

                last_sequence.append(fixed_sequence[x-1])

                print (last_sequence)

    print ("Last sequence:",last_sequence)

last_sequence(12)

# Next homework get an average of the sequence: plus each item and divide...
# Becareful with bugs for example zero numbers or values more that the sequence have
# Print 1000 items but the sequence have only 100.
# This method assume that you have a sequence, add sequence as parameter in future fixes.

# NOTES

        #print(x)

#print ("")
#print ("List length:" , len(fixed_sequence), "items.")

#print ("")
#print ("List items:" , fixed_sequence)


#for x in range (1,101):
        
        #print(fixed_sequence[1])

#print ("List 5 last items:" , fixed_sequence[94], fixed_sequence[99])