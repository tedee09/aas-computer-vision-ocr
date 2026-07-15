# License Plate OCR with Vision Language Model (LLaVA v1.5)

## Description
This project performs Optical Character Recognition (OCR) on vehicle license plate images using the LLaVA v1.5 model, running locally via LM Studio. The model takes an image and a prompt as inputs to recognize the contents of the license plate.

## Project Structure
```
aas/
├── test/                 # Folder containing license plate images
├── labels.csv            # Ground truth labels for the plates
├── ocr_predict.py        # Script to predict license plate contents
├── evaluate_results.py.py     # Script to evaluate the results (CER)
├── predictions.csv    # Final prediction output
```

## Tools Used
- LM Studio (GUI + API server for LLaVA)
- Python 3.11
- Libraries: `requests`, `pandas`, `Levenshtein`

## How to Run

### 1. Activate the LLaVA Model in LM Studio

- Open **LM Studio**.
- Click the **"Developer"** tab on the left side.
- Enable the **"Serve on Local Network"** option.
- Note the server port (e.g., `1234`).
- Click the **"Status"** tab and ensure the model status is **Running**.
- Open a browser and visit:

```
http://localhost:1234/v1/models
```
If the model is active, a response like this will appear:
```
JSON
{
  "data": [
    {
      "id": "llava-v1.5-7b",
      "object": "model",
      "owned_by": "organization_owner"
    },
    {
      "id": "text-embedding-nomic-embed-text-v1.5",
      "object": "model",
      "owned_by": "organization_owner"
    }
  ],
  "object": "list"
}
```

### 2. Run License Plate Prediction
Open a terminal and navigate to the project folder:

```
cd path/to/folder/aas
python ocr_predict.py
```

### 3. Evaluate CER Results
After the prediction is complete, run the evaluation:

```
python evaluate_results.py
```
The final results will be saved in the predictions.csv file, and the analysis output will be displayed in the terminal (number of predictions by category and the average CER).

CER Formula
CER = (S + D + I) / N
- S = substitution
- D = deletion
- I = insertion
- N = number of ground truth characters

## Evaluation Results
- Images tested: **168**
- Average CER: **~0.579**
- Results distribution:
  - Accurate: 10 images
  - Fair: 90 images
  - Failed: 68 images

### Accurate Prediction Example:
- Image         : test027_3.jpg
- Ground Truth  : L1840AL
- Prediction    : L1840
- CER Score     : 0.286

### Failed Prediction Example:
- Image         : test001_1.jpg
- Ground Truth  : B9140BCD
- Prediction    : B 9114116
- CER Score     : 0.750