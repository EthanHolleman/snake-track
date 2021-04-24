import subprocess
from pathlib import Path
from snake_track.write import *


def unlist_directory(dir_path):
    return list(Path(dir_path).list_dir())

def upload_files_to_s3_bucket(aws_exe, bucket_name, filepaths, output_path=None):
    bucket_link = f's3://{bucket_name}'
    bucket_links = []

    assert len(set(filepaths)) == len(filepaths), 'Filepaths are not unique!'

    if len(filepaths) == 1:  # could be file or directory
        if Path(filepaths[0]).is_dir():
            filepaths = unlist_directory()
    
    for filepath in filepaths:
        cmd = [aws_exe, 's3', 'cp', filepath, bucket_link]
        upload_url = f's3://{bucket_name}/{Path(filepath).name}'
        subprocess.run(cmd)
        bucket_links.append(filepath, upload_url)
    
    assert bucket_links, 'No data uploaded to S3 bucket!'

    if output_path:
        write_data_as_tsv(bucket_links, output_path)
        return output_path
    else:
        return data_to_tsv_string(bucket_links)
    



    
