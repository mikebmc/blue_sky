import pandas as pd
import numpy as np

read_file = 'tribeca_data_2016-06.csv'

intersection = np.array([40.720768, -74.010015])
half_block_from_int = np.array([40.720410, -74.010097])

radius = np.linalg.norm(half_block_from_int - intersection)

tribeca = pd.read_csv(read_file)
