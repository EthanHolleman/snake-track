import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--aws-path', default='aws', help='Path to aws exe. Default is aws.')
    subparsers = parser.add_subparsers()
    subparsers = upload_files_to_bucket(subparsers)
    args = parser.parse_args()
    return args

    
def upload_files_to_bucket(subparsers):
    upload_bucket = subparsers.add_parser('bucketUpload', help='Upload list of files to an existing S3 bucket')
    upload_bucket.add_argument('bucketName', metavar='B', help='Bucket to upload to')
    upload_bucket.add_argument('files', metavar='F', help='Filepaths to upload or directory of files to upload.', nargs='+')
    upload_bucket.add_argument('--tsv', metavar='OT', default=False, help='Output filepaths and S3 urls to a tsv file at this location. Else prints to stout')
    return subparsers

    

# def add_new_track_args(parser):
#     new_track = new_parser.add_subparser('newTrack')
#     parser.add_argument('--type', default='bigWig')
#     parser.add_argument('--visibility', default='full')
#     parser.add_argument('--priority', type=int, default=1)
#     parser.add_argument('--auto-scale', default='off', choices=['on', 'off'])
#     parser.add_argument('')

#     new_track.add_argument('trackTsv', help='Path to tsv file specifing track file paths')
#     new_track.add_argument('--shortLabel', help='Short label for hub')
#     new_track.add_argument('--longLabel', help='Extended track description')
#     new_track.add_argument('genomeFile', help='Path to genome file. Should specify the genome on line one and the trackDB file on line two.')





    