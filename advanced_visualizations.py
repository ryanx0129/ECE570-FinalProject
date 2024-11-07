import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def convert_classification_to_numeric(df):
    # Create a mapping for classification labels to numerical values
    classification_mapping = {
        "GOOD BOT": 0,
        "BAD BOT": 1,
        "Repeating Prompt": 2,
        "Irrelevant": 3,
        "UNCLEAR": 4
    }
    # Map classification labels to numeric values
    df['Classification_Numeric'] = df['Classification'].map(classification_mapping)
    return df

def plot_violin_plot(df):
    # Convert classification labels to numeric values for violin plot
    df = convert_classification_to_numeric(df)
    
    plt.figure(figsize=(12, 6))
    sns.violinplot(x="Obfuscation Method", y="Classification_Numeric", data=df)
    plt.title("Violin Plot of Classification by Obfuscation Method")
    plt.xlabel("Obfuscation Method")
    plt.ylabel("Classification (Numeric)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("violin_plot_classification.png")
    plt.show()

def plot_swarm_plot(df):
    # Convert classification labels to numeric values for swarm plot
    df = convert_classification_to_numeric(df)
    
    plt.figure(figsize=(12, 6))
    sns.swarmplot(x="Obfuscation Method", y="Classification_Numeric", data=df)
    plt.title("Swarm Plot of Classification by Obfuscation Method")
    plt.xlabel("Obfuscation Method")
    plt.ylabel("Classification (Numeric)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("swarm_plot_classification.png")
    plt.show()

def plot_classification_distribution(df):
    plt.figure(figsize=(8, 8))
    classification_counts = df["Classification"].value_counts()
    classification_counts.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
    plt.title("Overall Classification Distribution")
    plt.ylabel("")  # Hide y-axis label for better presentation
    plt.savefig("overall_classification_distribution.png")
    plt.show()

if __name__ == "__main__":
    # Load the CSV data
    df = pd.read_csv("adversarial_test_results.csv")

    # Plot visualizations
    plot_violin_plot(df)
    plot_swarm_plot(df)
    plot_classification_distribution(df)
