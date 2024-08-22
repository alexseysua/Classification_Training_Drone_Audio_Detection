import csv

def delete_rows_with_string(input_file_path, output_file_path, target_string):
    with open(input_file_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        rows = [row for row in reader if all(target_string not in cell for cell in row)]

    with open(output_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)

# Example usage:
delete_rows_with_string('mfcc_labels_all.csv', 'mfcc_labels_no_ours_no_abc.csv', 'ours_3')
delete_rows_with_string('mfcc_labels_no_ours_no_abc.csv', 'mfcc_labels_no_ours_no_abc.csv', 'A_data')
delete_rows_with_string('mfcc_labels_no_ours_no_abc.csv', 'mfcc_labels_no_ours_no_abc.csv', 'B_data')
delete_rows_with_string('mfcc_labels_no_ours_no_abc.csv', 'mfcc_labels_no_ours_no_abc.csv', 'C_data')
