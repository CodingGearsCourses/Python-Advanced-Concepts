# Copyright https://www.globaletraining.com/
# Dictionary comprehensions provide a concise way to create dictionaries.


def main():
    states = ["Texas", "California", "Colorado", "Arizona", "Georgia"]
    capitals = ["Austin", "Sacramento", "Denver", "Phoenix", "Atlanta"]

    # Creating a dictionary with key as the number and value as the squared of the number
    my_state_cap_dict = {}
    for state in states:
        for capital in capitals:
            if states.index(state) == capitals.index(capital):
                my_state_cap_dict[state] = capital
    print(my_state_cap_dict)

    # TODO: Using zip
    state_capitals = zip(states, capitals)
    print(dict(state_capitals))

    # TODO: Using Comprehension
    state_capitals_comp = {s: c for s in states for c in capitals if states.index(s) == capitals.index(c)}
    print(state_capitals_comp)


if __name__ == '__main__':
    main()