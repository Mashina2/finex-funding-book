# finex-funding-book
Simple script to output the offers in the Bitfinex funding book for USD.

This script uses the requests library to pull the funding data from the Bitfinex API.
It also uses the Rich library, in order to output the funding book as a table supporting color in the console.

To install the required libraries, on the console prompt run:

    pip install -r requirements.txt

The script has a parameters to control its behaviour:

    precision - The precision of the rate. This should be a value from 1 to 4. Default = 1

Running the script:

![image](https://user-images.githubusercontent.com/54691174/170951452-a9699f20-aeea-48df-8eba-50a735348a3d.png)
