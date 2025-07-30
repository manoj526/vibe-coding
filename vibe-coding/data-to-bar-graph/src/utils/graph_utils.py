def create_bar_graph(data):
    import matplotlib.pyplot as plt

    # Assuming data is a dictionary with keys as labels and values as counts
    labels = list(data.keys())
    values = list(data.values())

    plt.bar(labels, values)
    plt.xlabel('Labels')
    plt.ylabel('Values')
    plt.title('Bar Graph')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()