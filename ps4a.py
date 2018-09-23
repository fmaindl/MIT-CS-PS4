


def get_permutations(sequence):
   
    if len(sequence) == 1:
        return [sequence]
    
    result = []
    
    for i, let in enumerate(sequence):
        for p in get_permutations(sequence[:i] + sequence[i + 1:]):
            result = result + [let + p]

            
    return result
            

            


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

