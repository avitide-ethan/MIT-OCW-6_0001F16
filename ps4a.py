# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations_v2_wenwei(sequence):


    def insert_letter_into(letter, permutations):
        """
        :param letter: A single-letter string
        :param permutations: A list of strings
        :return: A list of strings
        """
        results = []
        for p in permutations:
            results.append(letter + p)
            results.append(letter + p)
            print(f'insert {letter} into {permutations}')
            # results.append(p + letter)
        return results

    def reduce(sequence):
        """
        Reduce the problem size
        :param sequence: A string
        :return:
        """
        if len(sequence) == 1:
            return [sequence]
        letter = sequence[0]
        remainder_string = sequence[1:]
        return insert_letter_into(letter, reduce(remainder_string))

    first_letter = sequence[0]
    remainder_string = sequence[1:]
    remainder_permutations = reduce(remainder_string)

    return insert_letter_into(first_letter, remainder_permutations)


def get_permutations_v3_ethan(sequence):

    # first create top level functions

    def create_permutation_list(letter, input_strings):
        """
        :param letter: a string that is one character
        :param input_strings: a list of strings
        :return: a list of strings
        """

        permutations = []
        for string in input_strings:
            # print(f"Insert letter into {string}")
            for charnum in range(0, len(string)+1):
                permutations.append(string[:charnum] + letter + string[charnum:])
        return permutations

    def reduce_problem_size(input_string):
        """
        :param input_string: a string
        :return: list of permutations of reduced problem
        """
        if len(input_string) == 1:
            return [input_string]
        reduced_letter = input_string[0]
        reduced_string = input_string[1:]
        return create_permutation_list(reduced_letter, reduce_problem_size(reduced_string))

    first_letter = sequence[0]
    first_permutations = sequence[1:]
    reduced_permutations = reduce_problem_size(first_permutations)
    return create_permutation_list(first_letter, reduced_permutations)



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

    if type(sequence) == str:
        sequence = [sequence]

    # returns first letter and the rest of the string
    def slice_first_letter(item):
        return item[0:1], item[1:len(item)]

    # method that inserts first character into item at all locations
    def insert_letter(letter, item):
        permutations = []
        for char_num in range(0, len(item)+1):
            append_string = item[:char_num] + letter + item[char_num:]
            print("Now working on char_num {}".format(char_num))
            print(append_string)
            permutations.append(append_string)
        print(permutations)
        return permutations

    def slice_and_insert(item):
        letter, item = slice_first_letter(item)
        return insert_letter(letter, item)

    if len(sequence[0]) == 1:
        return sequence[0]
    else:
        new_sequence = []
        for element in sequence:
            # print(slice_first_letter(element))
            new_sequence += slice_and_insert(element)
        return get_permutations(new_sequence)

    # recursive case
    # ABC
    # okay, greater than 1 letter
    # permute A into BC
    # BC is greater than 1 letter
    # permute B into C --> [BC, CB]
    # [ABC, BAC, CBA.... ACB CAB CBA]


# example_input = 'abc'
# print('Input:', example_input)
# print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
# print('Actual Output:', get_permutations(example_input))


# example_input = 'abc'
# print('Input:', example_input)
# print('Expected Output:', ['ab', 'ba'])
# print('Actual Output:', get_permutations(example_input))
#
# if __name__ == '__main__':
#     #    #EXAMPLE
#     #    example_input = 'abc'
#     #    print('Input:', example_input)
#     #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#     #    print('Actual Output:', get_permutations(example_input))
#
#     #    # Put three example test cases here (for your sanity, limit your inputs
#     #    to be three characters or fewer as you will have n! permutations for a
#     #    sequence of length n)
#
#     pass

if __name__ == '__main__':
    input_sequence = 'pickle'
    permutations = get_permutations_v3_ethan(input_sequence)
    print(f'The result of {input_sequence} is {permutations}')