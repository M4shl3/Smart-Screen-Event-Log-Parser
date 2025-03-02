# SmartScreen Event Log Parser

A Python tool to parse Windows SmartScreen Event Logs (`.evtx`) and extract execution details for files or executables. The tool processes the log file, filters relevant events, and outputs the results in a CSV file.

---

## Features

- Parses `.evtx` files containing SmartScreen event logs.
- Extracts details such as:
  - **Computer Name**
  - **User ID**
  - **Record Time**
  - **File Path**
  - **Execution Time**
- Filters events related to file executions (e.g., `isFileSupported`).
- Outputs results in a structured CSV file.

---

## Installation

### Prerequisites

- Python 3.6 or higher.
- `python-evtx` library for parsing `.evtx` files.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/M4shl3/Smart-Screen-Event-Log-Parser.git
   cd Smart-Screen-Event-Log-Parser
   ```

2. Install the required Python libraries:
   ```bash
   pip install python-evtx
   ```

3. Ensure the `.evtx` file you want to parse is available in the working directory or provide the full path to the file.

---

## Usage

### Command-Line Arguments
The script accepts two arguments:

- **Input File**: Path to the `.evtx` file.
- **Output File**: Path to the output CSV file.

### Example
To parse a SmartScreen log file and save the results to a CSV file:
   ```bash
   python smartscreen_parser.py Microsoft-Windows-SmartScreen.evtx output_results.csv
   ```

