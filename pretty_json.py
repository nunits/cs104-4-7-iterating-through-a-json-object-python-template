def main():
    data = [
        # JSON data copied from Postman for the word "baby"
        {"word": "little", "score": 1001},
        {"word": "crying", "score": 1000},
        {"word": "adorable", "score": 999},
        {"word": "cute", "score": 998},
        {"word": "sweet", "score": 997},
        {"word": "sleepy", "score": 996}
    ]

    adjectives = []  # Create an empty list

    # TODO: Iterate over the data and extract the adjectives for the word and store them in the list variable
    for item in data:
        adjectives.append(item["word"])

    # TODO: Print the list variable, Example of print: Adjectives for the word "word" are: [list of adjectives]
    print('Adjectives for the word "baby" are:', adjectives)


if __name__ == '__main__':
    main()