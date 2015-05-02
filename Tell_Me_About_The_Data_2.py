import csv

from StringIO import StringIO
import pandas as pd

import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

PATH = 'data/hotel.csv'

if __name__ == '__main__':
    # Read and open the CSV file
    with open(PATH, 'r') as f:
        data   = StringIO() # Create a temporary holder for string data
        reader = csv.DictReader(f) # Read the CSV data
        writer = csv.DictWriter(data, fieldnames=reader.fieldnames) # Create a writer to write new csv data
        writer.writeheader() # Write the header line

        # For each row, do the wrangling

        for row in reader:
            newrow = {}
            for key, val in row.items():

                val = val.strip() # Strip white space
                val = val.replace('%', '') # Remove percents
                val = val.replace('$', '') # Remove dollar signs
                newrow[key] = val

            # write the row to our temporary data

            writer.writerow(newrow)

        # Reset the String IO

        data.seek(0)

    # Plot the scatter matrix

    df = pd.read_csv(data)
    scatter_matrix(df, alpha=0.2, diagonal='kde')
    plt.show()