# finex-funding-book
Simple script to output the offers in the Bitfinex funding book for USD.
It also outputs any significant walls detected at the end of the output (where the cumulative amount has changed over 200%, and the previous cumulative amount is at least 1 million).

This script uses the requests library to pull the funding data from the Bitfinex API.
It also uses the Rich library, in order to output the funding book as a table supporting color in the console.

To install the required libraries, on the console prompt run:

    pip install -r requirements.txt

The script has a parameters to control its behaviour:

    precision - The precision of the rate. This should be a value from 1 to 4. Default = 1

Running the script:

![image](https://user-images.githubusercontent.com/54691174/170957460-0f648cf9-f520-4738-b7d7-1627cc7479fc.png)
