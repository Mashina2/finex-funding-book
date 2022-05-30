# finex-funding-book
Simple script to output the offers in the Bitfinex funding book for USD.
It also outputs any significant walls detected at the end of the output (where the cumulative amount has changed over 200%, and the previous cumulative amount is at least 1 million).

This script uses the requests library to pull the funding data from the Bitfinex API.
It also uses the Rich library, in order to output the funding book as a table supporting color in the console.

To install the required libraries, on the console prompt run:

    pip install -r requirements.txt

The script has one parameter to control its behaviour:

    precision - Precision of the rate. Should be a value from 0 - 4. Lower value means higher precision. Default = 4

Running the script:

![image](https://user-images.githubusercontent.com/54691174/170968694-754feb73-803d-4adb-aca8-9b3816f22009.png)
