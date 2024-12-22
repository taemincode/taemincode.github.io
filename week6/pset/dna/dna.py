import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: dna.py databases sequences")
        return

    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], 'r') as file:
        sequence = file.readline()

    # TODO: Find longest match of each STR in DNA sequence
    dict = {}
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        subsequences = reader.fieldnames

    for i in range(len(subsequences) - 1):
        dict[subsequences[i + 1]] = longest_match(sequence, subsequences[i + 1])

    # TODO: Check database for matching profiles
    for i in range(len(rows)):
        for j in range(len(subsequences) - 1):
            if rows[i][subsequences[j + 1]] != str(dict[subsequences[j + 1]]):
                break
            if j == len(subsequences) - 2:
                print(rows[i]['name'])
                return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
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
