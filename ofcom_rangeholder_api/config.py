import os

package_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(package_dir, 'data')

remote_data_files = [
    'http://static.ofcom.org.uk/static/numbering/s1_code.txt',
    'http://static.ofcom.org.uk/static/numbering/s3_code.txt',
    'http://static.ofcom.org.uk/static/numbering/s5_code.txt',
    'http://static.ofcom.org.uk/static/numbering/s7_code.txt',
    'http://static.ofcom.org.uk/static/numbering/s8_code.txt',
    'http://static.ofcom.org.uk/static/numbering/s9_code.txt'
]
