# Step 1 : Defining the Probelm : we need to write a program to iterate through a list of numbers arranged in descending order and find the position of the given number and return -1 if it's not found

#Step 2: Writing the inputs : cards for list and query for the given num
#make a function with params
def card_locater(cards, query):
    for index in range(len(cards)):
        if cards[index] == query:
            return index

    return -1


#now we try to make test cases
test =[ { 'input': {'cards': [12,11,10,7,2,0] , 'query': 7 }, 'output' : 3},
        {'input': {'cards': [7,6,5] , 'query': 7 }, 'output' : 0},#first element
        {'input': {'cards': [50,40,7] , 'query': 7 }, 'output' : 2},#last element
        {'input': {'cards': [60,7,7,7,20] , 'query': 7 }, 'output' : 1},#multiple elements
        {'input': {'cards': [] , 'query': 7 }, 'output' : -1} #Empty list
        ]
#now to test it
for i, case in enumerate(test):
    print("running test" , i+1)
    result = card_locater(**case['input'])
    if result == case['output']:
        print("passed")
    else:
        print("failed")
""" Now what do I need to do:
Iterate through the list and if the given number is equal to query then return its index nor than 0
"""


