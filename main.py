file_path = "books/frankenstein.txt"

def main():
    report = produce_report(file_path)
    print(report)

def produce_report(file_path):
    book_text = get_book_text(file_path).lower()
    word_count = get_number_of_words(book_text)
    character_counts = get_sorted_character_counts(book_text)
    
    report = ""
    # TODO: Make the number of dashes in the header row dynamically match the given file path, maybe, as a treat???
    report += f"------------------------------------------------------------\n"
    report += f"--- Character Counts Report for '{file_path}' ---\n"
    report += f"------------------------------------------------------------\n"
    report += "\n"
    report += f"The document contains {word_count} words. \n"
    report += "\n"
    
    for item in character_counts:
        character = item["character"]
        count = item["count"]
        report += f"The '{character}' character was found {count} times. \n"

    report += "\n"
    report += f"------------------------------------------------------------\n"
    report += f"------------------------ End report ------------------------\n"
    report += f"------------------------------------------------------------\n"

    return report

def get_book_text(file_path):
    with open(file_path) as opened_file:
        book_text = opened_file.read()
        return book_text

def get_number_of_words(book_text):
    list_of_words = book_text.split()
    number_of_words = len(list_of_words)
    return number_of_words

def get_sorted_character_counts(text):
    # Get the text
    text = text.lower()
    
    # Create an empty list
    character_counts = []

    # And while we're at it, one to record the characters we've already handled
    characters_already_handled = []

    # For each character in the text...
    for character in text:
        # If it's not a letter, skip it
        if not character.isalpha():
            continue
        
        # If it's already been counted and recorded, skip it
        if character in characters_already_handled:
            continue
        
        # Otherwise, count how many times it appears...
        count = text.count(character)
        # And add to the list a dictionary (not a dictionary ENTRY, but an entire dictionary) which represents the character and its count. Again: each entry on the list is an ENTIRE dictionary, representing one character and its count.
        character_counts.append({
            "character":character,
            "count":count
        })

        # Record that we've handled that character...
        characters_already_handled.append(character)

    # ...and repeat for all the other characters, until we've constructed our entire list.

    # Next, let's sort the list.
    
    # First, we need to define a function that will, when given an individual item from the list (that is, a single dictionary representing one character and its count), extract and return the key which should be used for sorting: that is, in this case, the count.
    def get_sorting_key(dictionary_of_character_and_count):
        return dictionary_of_character_and_count["count"]

    # Now, we pass that function as an argument to one of Python's built-in sorting functions:
    character_counts.sort(reverse=True, key=get_sorting_key)

    return character_counts

main()