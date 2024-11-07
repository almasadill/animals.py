animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey'] 
animals['d'].append('dog') 
animals['d'].append('dingo') 
def biggest(c):
    biggestkey = None
    biggestlength = 0
    for key, values in c.items():
        if len(values) > biggestlength:
            biggestlength=len(values)
            biggestkey = key
    print("'"+str(biggestkey)+"'")
biggest(animals)

 