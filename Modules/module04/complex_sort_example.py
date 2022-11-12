"""
Showing how to sort using a custom function
Adopted from the section:
https://realpython.com/sort-python-dictionary/#selecting-a-nested-value-with-a-sort-key
"""

def main():
    """
    Business Logic
    n this example, you have a dictionary with numeric keys and a nested dictionary as a value.
    You want to sort by the combined Python and JavaScript skills, attributes found in the skills
    subdictionary.
    """
    data = {
        193: {"name": "John", "age": 30, "skills": {"python": 8, "js": 7}},
        209: {"name": "Bill", "age": 15, "skills": {"python": 6}},
        746: {"name": "Jane", "age": 58, "skills": {"js": 2, "python": 5}},
        109: {"name": "Jill", "age": 83, "skills": {"java": 10}},
        984: {"name": "Jack", "age": 28, "skills": {"c": 8, "assembly": 7}},
        765: {"name": "Penelope", "age": 76, "skills": {"python": 8, "go": 5}},
        598: {"name": "Sylvia", "age": 62, "skills": {"bash": 8, "java": 7}},
        483: {"name": "Anna", "age": 24, "skills": {"js": 10}},
        277: {"name": "Beatriz", "age": 26, "skills": {"python": 2, "js": 4}},
    }
    print(sorted(data.items(), key=get_relevant_skills, reverse=True))
    print("\n\n")

    # You didn’t use a lambda function in this example. While it’s possible, it would make for a
    # long line of potentially cryptic code:
    print(sorted(
        data.items(),
        key=lambda item: (
                item[1]["skills"].get("python", 0)
                + item[1]["skills"].get("js", 0)
        ),
        reverse=True,
    ))
    print("\n\n")
    # A lambda function can only contain one expression, so you repeat the full look-up in the
    # nested skills subdictionary. This inflates the line length considerably.
    #
    # The lambda function also requires multiple chained square bracket ([]) indices, making it
    # harder to read than necessary. Using a lambda in this example only saves a few lines of
    # code, and the performance difference is negligible. So, in these cases, it usually makes
    # more sense to use a normal function.


    # Converting Back to a Dictionary
    # The only issue left to address with the default behavior of sorted() is that it returns a
    # list, not a dictionary. There are a few ways to convert a list of tuples back into a dictionary.
    #
    # We can use a dictionary comprehension to do this
    sorted_dict = {key: value for key, value in sorted(data.items(), key=get_relevant_skills, reverse=True)}
    print(sorted_dict)


def get_relevant_skills(item):
    """
    Get the sum of Python and JavaScript skill
    @param item: Tuple coming from the dictionary
    @return: Int
    """
    # item here is a tuple like:
    # (193, {'name': 'John', 'age': 30, 'skills': {'python': 8, 'js': 7}})
    # so the 1 index is a dictionary and then we access "skills"
    skills = item[1]["skills"]
    # Return default value that is equivalent to no skill
    # Part of what makes sorting by the combined skill tricky is that the python and js keys aren’t
    # present in the skills dictionary for all people. The skills dictionary is also nested.
    # You use .get() to read the keys and provide 0 as a default value that’s used for missing skills.
    return skills.get("python", 0) + skills.get("js", 0)


if __name__ == '__main__':
    main()