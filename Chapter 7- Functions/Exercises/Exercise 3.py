'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

arguments to make a shirt. Call the function a second time using keyword arguments.'''

def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')