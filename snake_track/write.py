import csv

def write_data_as_tsv(data, output_path):
    with open(str(output_path), 'w') as handle:
        writer = csv.writer(handle, delimiter='\t')
        for row in data:
            writer.writerow(row)
    return output_path


def data_to_tsv_string(data):
    tsv_string = ''
    for row in data:
        data_row_string = '\t'.join([str(d) for d in data])
        tsv_string += (f'{data_row_string}\n')
    return tsv_string
