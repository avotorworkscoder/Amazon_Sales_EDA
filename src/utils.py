def save_plot(name):
    import os
    import matplotlib.pyplot as plt
    os.makedirs("outputs/plots", exist_ok=True)
    plt.savefig(f"outputs/plots/{name}.png", dpi=300, bbox_inches="tight")
