import time


#FUNCTIONS
def fixed_sequence(sequence_length:int):
       
        fixed_sequence = []

        for x in range (1,101):
                #time.sleep(.01)
                fixed_sequence.append(x)

        return fixed_sequence

def last_sequence(sequence:list,last_sequence_length:int):

    # Function that creates a new sequence from an existent sequence.
    # This new sequence get the last x number of items from that existent sequence.
    # x defines how many items you want to extract.

        sq_sequence = sequence
        sl = last_sequence_length-1

        last_sequence = []

        for x in sq_sequence:
                
                if x >= len(sq_sequence)-sl:

                        last_sequence.append(sq_sequence[x-1])

                        #print (last_sequence)

        #print ("Last sequence:",last_sequence)

        return last_sequence    

def average_sequence(sequence:list,sequence_length:int):
      
        sq_sequence = sequence
        #sq_sequence_length = sequence_length-1
        sq_sequence_length = len(sq_sequence)

        # Last Sequence Logic

        last_sequence = []

        for x in sq_sequence:
                
                if x >= len(sq_sequence)- sq_sequence_length:

                        last_sequence.append(sq_sequence[x-1])

                        #print (last_sequence)

                        #print ("Last sequence:",last_sequence)

        # Average Sequence Logic

        average_sequence = []

        result = 0
        last_sum = 0

        for x in range (0,len(last_sequence)):

                if x == 0:
                        preview_item = 0
                        actual_item = last_sequence[x]
                        item_sum = preview_item + actual_item
                        #print ("(index:", x,")","(         p + n = result)", "-","+", preview_item,"+" ,actual_item,"=",item_sum)

                else:
                        preview_item = item_sum
                        actual_item = last_sequence[x]
                        item_sum = preview_item + actual_item
                        average = item_sum / x+1
                        #print (round(average,2),"(index:", x,")","(result + p + n = result)",preview_item,"+" ,actual_item,"=",item_sum)

        return average

# EXECUTION

my_fixed_sequence = fixed_sequence(100)
my_last_sequence = last_sequence(my_fixed_sequence,10)
my_average_sequence = average_sequence(my_last_sequence,10)


print(my_fixed_sequence)
print(my_last_sequence)
print(my_average_sequence)


# NOTES
# Becareful with bugs for example zero numbers or values more that the sequence have
# Print 1000 items but the sequence have only 100.
# This method assume that you have a sequence, add sequence as parameter in future fixes.