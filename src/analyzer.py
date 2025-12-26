import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Data loaded successfully")

    def clean_data(self):
        self.df = self.df.dropna()
        print("Missing values removed")

    def analyze(self):
        return self.df.describe()

    def save_summary(self, summary):
        Path("output").mkdir(exist_ok=True)
        with open("output/summary.txt", "w") as f:
            f.write(summary.to_string())

    def plot_data(self):
        self.df.hist(figsize=(10, 8))
        plt.tight_layout()
        plt.savefig("output/plots.png")
        plt.close()

def main():
    analyzer = DataAnalyzer("data/sample_data.csv")
    analyzer.load_data()
    analyzer.clean_data()
    summary = analyzer.analyze()
    analyzer.save_summary(summary)
    analyzer.plot_data()

if __name__ == "__main__":
    main()
