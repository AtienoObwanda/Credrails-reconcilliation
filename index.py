import argparse
import csv
from typing import Dict, List, Tuple

def read_csv(file_path: str) -> List[Dict]:
    """
    Read CSV file and return list of dictionaries representing rows.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        List[Dict]: List of dictionaries representing rows in the CSV file.
    """
    rows = []
    with open(file_path, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows

def reconcile(source_file: str, target_file: str, output_file: str, compare_columns: List[str] = None) -> Tuple[int, int, int]:
    """
    Reconcile two CSV files and generate a reconciliation report.
    
    Args:
        source_file (str): Path to the source CSV file.
        target_file (str): Path to the target CSV file.
        output_file (str): Path to save the output reconciliation report.
        compare_columns (List[str], optional): Columns to compare (default is None).
        
    Returns:
        Tuple[int, int, int]: A tuple containing counts of records missing in target, missing in source, and discrepancies.
    """
    source_data = read_csv(source_file)
    target_data = read_csv(target_file)

    # Preparing data structures to store reconciliation results
    missing_in_target = []
    missing_in_source = []
    field_discrepancies = []

    # Converting target data to a dictionary for faster lookup
    target_dict = {record['ID']: record for record in target_data}

    # Comparing records between source and target
    for record in source_data:
        record_id = record['ID']
        if record_id not in target_dict:
            missing_in_target.append(record_id)
        else:
            target_record = target_dict[record_id]
            for column in record.keys():
                if compare_columns is None or column in compare_columns:
                    if record[column] != target_record[column]:
                        field_discrepancies.append((record_id, column, record[column], target_record[column]))

    for record in target_data:
        record_id = record['ID']
        if record_id not in {row['ID'] for row in source_data}:
            missing_in_source.append(record_id)

    # Writing reconciliation report to CSV file
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Type', 'Record Identifier', 'Field', 'Source Value', 'Target Value'])
        for record_id in missing_in_target:
            writer.writerow(['Missing in Target', record_id, '', '', ''])
        for record_id in missing_in_source:
            writer.writerow(['Missing in Source', '', record_id, '', ''])
        for record_id, column, source_value, target_value in field_discrepancies:
            writer.writerow(['Field Discrepancy', record_id, column, source_value, target_value])

    return len(missing_in_target), len(missing_in_source), len(field_discrepancies)

def main():
    parser = argparse.ArgumentParser(description='CSV Reconciler')
    parser.add_argument('-s', '--source', type=str, help='Path to source CSV file', required=True)
    parser.add_argument('-t', '--target', type=str, help='Path to target CSV file', required=True)
    parser.add_argument('-o', '--output', type=str, help='Path to save the output reconciliation report', required=True)
    parser.add_argument('-c', '--compare', nargs='+', help='Columns to compare (optional)', required=False)
    args = parser.parse_args()

    missing_in_target, missing_in_source, discrepancies = reconcile(args.source, args.target, args.output, args.compare)

    print("Reconciliation completed:")
    print(f"- Records missing in target: {missing_in_target}")
    print(f"- Records missing in source: {missing_in_source}")
    print(f"- Records with field discrepancies: {discrepancies}")
    print(f"Report saved to: {args.output}")

if __name__ == "__main__":
    main()
