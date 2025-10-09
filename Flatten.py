'''Flatten'''
import json

def flatten_list(nested_list):
    """
    Recursively flattens a list that may contain other lists.
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            # If the item is a list, extend the flat_list with the flattened version of it
            flat_list.extend(flatten_list(item))
        else:
            # If the item is not a list, just append it
            flat_list.append(item)
    return flat_list

def main():
    '''main'''
    try:
        # Use json.loads() to safely parse the string input into a Python list
        nested_list = json.loads(input())
        flat_list = flatten_list(nested_list)
        if flat_list:
            print(sorted(flat_list, reverse=True))
    except (json.JSONDecodeError, TypeError):
        # Handle cases where input is not a valid list format
        print("Invalid input.")
if __name__ == "__main__":
    main()
