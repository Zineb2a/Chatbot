# Chatbot

## Project Description

The project I developed is a ChatBot coded in Python with a MySQL database. A chatbot is a computer program designed to simulate a written conversation with a human user. I did not attempt to extract the meaning of the sentences written by the user. The program is divided into two parts:

### Learning:
When the user types a message, it is understood as a response to a previous statement made by the chatbot. The sentence typed by the human will then be associated with the words present in the previous message.

### Response:
The human's message is broken down into words. The program will try to identify the sentences that best match these words based on its previous "experience." The intelligent robot will store word associations (Sentences) as a response to a given sentence from the user and will use them to try to match future responses.

## How to Use This Code?

1. Ensure you have Python installed on your system.
2. Create a MySQL database and name it 'bdd.sqlite'.
3. Run the provided Python code.
4. Start interacting with the ChatBot by entering messages.
5. The ChatBot will learn from your responses and provide answers based on its previous learnings.

## Dependencies

The code uses the following Python libraries:

- `re`: For using regular expressions. [Documentation](https://docs.python.org/3/library/re.html)
- `sqlite3`: For managing the SQLite database. [Documentation](https://docs.python.org/3/library/sqlite3.html)
- `collections.Counter`: For counting word occurrences. [Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)
- `string.punctuation`: For handling punctuation marks. [Documentation](https://docs.python.org/3/library/string.html#string.punctuation)
- `math.sqrt`: For performing mathematical calculations. [Documentation](https://docs.python.org/3/library/math.html#math.sqrt)
