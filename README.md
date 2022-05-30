# finex-funding-book
Simple script to output the offers in the Bitfinex funding book for USD.

This script uses the requests library to pull the funding data from the Bitfinex API.
It also uses the Rich library, in order to output the funding book as a table supporting color in the console.

To install the required libraries, on the console prompt run:

    pip install -r requirements.txt

The script has a parameters to control its behaviour:

    precision - The precision of the rate. This should be a value from 1 to 4. Default = 1

Running the script:

![image](https://user-images.githubusercontent.com/54691174/170957013-214a7d86-e9f7-469f-9ecd-2fcf2f27d2a6.png)
