

# Random Password Generator

This is the starting point of the random password generator project. Currently its purpose is to generate passwords between 4 and 16 characters, following the best practices of including special characters, upper-case letters and numbers in a randomly fashion.

## How to Install and Run the Project

1. Clone the repository.
	`git clone git@github.com:keremidarski/random_password_generator.git`

2. Install the dependencies.
	`pip3 install -r requirements.txt`

3. Run the app.
	`python3 main.py`

## How to Use the Project

1. Input the desired password length *(between 4 and 16 symbols)*.
2. Click the "**Generate**" button.
3. The generated password is displayed below the button.
	- You can select the text by mouse or use the "**Copy to Clipboard**" button.

## Tests

There is a `tests.py` file which contains tests that ensure that the generator produces unique passwords every time.

## License

MIT License

Copyright (c) 2022 Ivaylo Keremidarski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

