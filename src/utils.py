def save_plot(name):
    import os
    import matplotlib.pyplot as plt
    os.makedirs("output/plots", exist_ok=True)
    plt.savefig(f"output/plots/{name}.png", dpi=300, bbox_inches="tight")
