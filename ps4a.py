# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """



    # method that inserts first character into permutation of remaining characters
    def permutations_into_an_item(letter, item):



    # base case
    sequence = [sequence]
    if len(sequence[0]) == 1:
        return sequence
    # recursive case
    # A
    # AB, BA
    # CAB, ACB, ABC... CBA, BCA, BAC
    else:
        for letter in se:n= sequence[0]
        sequence_for_permutations = sequence[1:len(sequence)]
        print("Sequence for permutations: {}, Letter: {}".format(sequence_for_permutations, letter))
        permutation_list = []
        for item in range(0, len(sequence_for_permutations)):
            permutation_list.append(sequence_for_permutations[:item] + letter + sequence_for_permutations[item:])
            # iterate over sequence_for_permutations, inserting item into each location
        return get_permutations(permutation_list)


        # for x in range(len(sequence)):
        #     pass
        # pop the first letter
        # get permutations of what's left
        # return sequence
    # permutation abcd = a into permutation bcd = b into permutation cd = c into d



example_input = 'abc'
print('Input:', example_input)
print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
print('Actual Output:', get_permutations(example_input))

if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    pass

