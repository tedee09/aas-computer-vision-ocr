import pandas as pd

# Read the prediction results file
df = pd.read_csv("prediction_results.csv")

# Function to categorize results based on CER
def categorize_cer(cer):
    if cer <= 0.3:
        return "Accurate"
    elif cer <= 0.6:
        return "Fair"
    else:
        return "Failed"

# Add category column to dataframe
df["category"] = df["CER_score"].apply(categorize_cer)

# Display classification results
print("Number of predictions per category:")
print(df["category"].value_counts())
print()

# Display average CER
print(f"Average CER: {df['CER_score'].mean():.3f}")

# Examples of accurate and failed predictions
accurate_example = df[df["category"] == "Accurate"].iloc[0]
failed_example = df[df["category"] == "Failed"].iloc[0]

print("\n📌 Accurate Prediction Example:")
print(f"Image         : {accurate_example['image']}")
print(f"Ground Truth  : {accurate_example['ground_truth']}")
print(f"Prediction    : {accurate_example['prediction']}")
print(f"CER Score     : {accurate_example['CER_score']:.3f}")

print("\n📌 Failed Prediction Example:")
print(f"Image         : {failed_example['image']}")
print(f"Ground Truth  : {failed_example['ground_truth']}")
print(f"Prediction    : {failed_example['prediction']}")
print(f"CER Score     : {failed_example['CER_score']:.3f}")