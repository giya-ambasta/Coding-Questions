def main():
    # Read number of scores
    N = int(input())
    
    # Read scores as a string and split
    scores_input = input().split()
    
    # Convert scores to integers
    scores = [int(score) for score in scores_input]
    
    # Write scores to file
    with open('scores.txt', 'w') as file:
        for score in scores:
            file.write(str(score) + '\n')
    
    # Read scores from file and filter high scores
    high_scores = []
    with open('scores.txt', 'r') as file:
        for line in file:
            score = int(line.strip())
            if score >= 90:
                high_scores.append(score)
    
    # Print results
    if high_scores:
        print(' '.join(map(str, high_scores)))
    else:
        print('0')

# Execute the program
if __name__ == "__main__":
    main()
