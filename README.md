# Credrails Reconcilliation Program
---

This is a tool that will read in two CSV files (termed "source" and "target"), reconcile the records, and produce a report detailing the differences between the two.


# Step-by-Step Instructions to Run the CSV Reconciliation Tool
---
### Step 1: Clone the Repository
Clone the repository containing the CSV reconciliation tool to your local machine. You can do this by running the following command in your terminal:
SSH:
 
 ```
 git clone git@github.com:AtienoObwanda/Credrails-reconcilliation.git
 ```

 HTTPS:
 
 ```
 git clone https://github.com/AtienoObwanda/Credrails-reconcilliation.git
 ```

 OR GITHUB CLI:

 ```
 git clone gh repo clone AtienoObwanda/Credrails-reconcilliation
 ```
---

 ### Step 2: Install Python
Ensure you have Python installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/). Make sure to add Python to your system PATH during installation.

---

### Step 3: Install Dependencies
Navigate to the root directory of the cloned repository in your terminal. Then, install the required dependencies by running:

```
pip install -r requirements.txt
```

---

### Step 4: Run the Tool via Command Line
You can run the CSV reconciliation tool from the command line interface (CLI). Use the following command syntax:

```
python index.py -s source.csv -t target.csv -o reconciliation_report.csv -c Date Amount
```

---

### Step 5: Run the Tool via Graphical User Interface (GUI)
Alternatively, you can run the CSV reconciliation tool using the graphical user interface (GUI). Run the following command:

```
python gui.py
```

This will launch a GUI window where you can browse and select your source CSV file, target CSV file, and specify the output report path. Click the "Run Reconciliation" button to initiate the reconciliation process.

---

### Step 6: View Results
After running the tool, you will receive a reconciliation report containing information about records missing in the target, records missing in the source, and records with field discrepancies. You can view this report in your specified output location.

---

### Step 7: Running Tests (Optional)
If you want to run tests to ensure the tool's functionality, you can do so by running:

```
python test.py
```


This will execute the unit tests and provide feedback on whether the tool is functioning as expected.

---

That's it! You've successfully run the CSV reconciliation tool. If you encounter any issues or have questions, feel free to reach out for further assistance.