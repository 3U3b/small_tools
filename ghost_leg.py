# import random
import numpy as np

# ------------------------
def generate_subladders(width, step_char, rail_char, spacer_char, item_number):

    probabilities = [1/item_number, (item_number-1)/item_number]
    values = [True,  False]

    subladders = []
    for i in range(item_number-1):
        result = np.random.choice(values, p=probabilities)

        if result:
            subladders.append(f'{step_char * width}{rail_char}')
        else:
            probabilities[0] = 1/(item_number-(i+1))
            probabilities[1] = (item_number-(i+2))/(item_number-(i+1))
            subladders.append(f'{spacer_char * width}{rail_char}')


    return subladders
# ------------------------

def print_all_ladders(width, step_char, rail_char, spacer_char, height, item_number):

    sw = 1
    tops = []
    values = ['ＹＯ', 'ＮＯ']
    probabilities = [1/item_number, (item_number-1)/item_number]

    for i in range(item_number):
        result = np.random.choice(values, p=probabilities)

        if (result == values[0]) & sw == 1:
            sw = 0
            tops.append(result)
#            print("Y",'\n',i)
        elif sw == 0:
            tops.append(values[1])
#            print("N",'\n',i)
        else:
#            print("N",'\n',i)
            probabilities[0] = 1/(item_number-(i+1))
            probabilities[1] = (item_number-(i+2))/(item_number-(i+1))
            tops.append(result)

#    GOOO_L = ('{:<6}'.format(top) )
    GOOO = ''.join(f'{top}{spacer_char * (width-1)}' for top in tops)
    print(GOOO)

    addladders = [generate_subladders(width, step_char, rail_char, spacer_char,item_number) for _ in range(height)]
    for i in range(height):
        print(rail_char,end='')
        print(''.join(addladders[i]))


#    parts = ['{:<6}'.format(chr(ch))for ch in range(0xFF21, 0xFF3B)]
#    range(0xFF21, 0xFF3B) == range(65, 91) == A~Z
    parts = [chr(ch) for ch in range(0xFF21, 0xFF3B)]
    selected_parts = parts[:item_number]

#    selected_parts = chr(for ch in range(65, 91))
    bottom_row = ''.join(f'{part}{spacer_char * (width)}' for part in selected_parts)
    print(bottom_row)



try:
    width = 3
    step_char = "ㄧ"
    rail_char = "｜"
    spacer_char = '\u3000'
    item_number = int(input("How many items ?(upper limit to 26 items): "))
    ladder_height = item_number*3

    print_all_ladders(width, step_char, rail_char, spacer_char, ladder_height, item_number)
except ValueError as e:
    print(e)
