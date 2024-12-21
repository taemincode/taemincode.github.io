import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv[]) != 3:
        print("Usage: dna.py databases sequences")
        return

    # TODO: Read database file into a variable
    rows = []
    with open(argv[2]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    with file = open(argv[3], 'r'):
        sequence = file.readline()

    # TODO: Find longest match of each STR in DNA sequence
    dict = {}
    with open(argv[2]) as file:
        reader = csv.DictReader(file)
        for i in range(len(reader.fieldnames) - 1):
            dict[reader.fieldnames[i + 1]]  = longest_match(sequence, reader.fieldnames[i + 1])

    # TODO: Check database for matching profiles

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    match = False

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        for j in range(subsequence_length):
            if sequence[i + j] != subsequence[j]:
                break
            if j == subsequence_length:
                match = True

        # If a match, move substring to next potential match in sequence
        if match == True

        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
