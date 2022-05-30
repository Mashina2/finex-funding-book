import argparse
import requests
from rich.console import Console
from rich.table import Table
from rich import print

def output_funding(precision, ):
    # Validate precision
    if precision < 0 or precision > 4:
        print("Invalid precision. Please use a value between 0 and 4.")
        return

    funding_url = f"https://api-pub.bitfinex.com/v2/book/fUSD/P{precision}?len=250"
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
        request_headers = {'User-Agent': user_agent}
        session = requests.session()
        response = session.get(funding_url, headers=request_headers, timeout=60)
        if response.status_code != requests.codes.ok:
            print(f"Unable to request funding. {response.text}")
            return
        
        funding_raw = response.json()

        table = Table(show_header=True, header_style="bold")
        table.add_column("RATE")
        table.add_column("PERIOD")
        table.add_column("COUNT")
        table.add_column("AMOUNT")
        table.add_column("CUM. AMT")

        cumulative_amount = 0
        for funding_record in funding_raw:
            # Only output funding for offers (i.e. where the amount is a positive value)
            
            if funding_record[3] > 0:
                cumulative_amount += funding_record[3]
                table.add_row(  f"[green]{round(funding_record[0] * 100, 6):.6f}[/green]", 
                                f"[green]{funding_record[1]}[/green]", 
                                f"[green]{funding_record[2]}[/green]", 
                                f"[green]{round(funding_record[3], 2):.2f}[/green]",
                                f"[green]{round(cumulative_amount, 2):.2f}[/green]")

        console = Console()      
        console.print(table)

    except Exception as ex:
        print(f"An error occurred: {str(ex)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Define the precision argument to control funding rate precision on the offer side.')
    parser.add_argument('--precision', 
                        type=int,
                        default=1,
                        help='Rate Precision. From 0 - 4. Default = 1')
    args = parser.parse_args()

    output_funding(args.precision)