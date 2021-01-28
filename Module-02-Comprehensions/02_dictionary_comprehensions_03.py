# Copyright https://www.globaletraining.com/
# Dictionary comprehensions provide a concise way to create dictionaries.


def main():
    scores = {'Texas': 11, 'California': 30, 'Colorado': 49, 'Arizona': 33, 'Florida': 55}

    # Creating a dictionary with squared values
    # for item in scores:
    #     scores[item] *= 2
    # print(scores)

    # TODO: Using Comprehension
    # scores_comp1 = {key: value * 2 for (key, value) in scores.items()}
    # print(scores_comp1)

    # TODO: Using Comprehension & Conditions (2)
    # scores_comp2 = {key: value * 2 for (key, value) in scores.items() if value <=50 if value !=49}
    # print(scores_comp2)

    # TODO: Using Comprehension & Conditions (3)
    scores_comp3 = {key: value * 2 for (key, value) in scores.items() if value <=50 if value !=49 if value != 10}
    print(scores_comp3)

if __name__ == '__main__':
    main()