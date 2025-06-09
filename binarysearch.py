"""How do i apply binary search
1) Find the middle element
2) See if that matches the given number
3) If it is bigger than the req no. search for the right
4) If it is smaller then search for the left
5)If nothing remains return -1"""

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid -1 >= 0 and cards[mid -1] == query:
            return "left"
        else:
            return "found"
    elif cards[mid] < query:
        return "left"
    else:
        return "right"

def card_locater(cards, query):
      low = 0
      high = len(cards)-1
      while low<= high:
          mid_index = (low+ high)//2
          mid_number = cards[mid_index]
          result = test_location(cards, query, mid_index)
          if result == "found":
              return mid_index
          elif result == "left":
              high =  mid_index -1
          else:
              low = mid_index + 1
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


