import pandas as pd
import matplotlib.pyplot as plt
from utils.graph_utils import create_bar_graph

def main():
    # Sample data
    data = {
        'Categories': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 15, 25]
    }
    
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Create a bar graph
    create_bar_graph(df)

if __name__ == "__main__":
    main()
