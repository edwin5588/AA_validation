import os
import subprocess
import pysftp

def execute(cmd):
    """
    executes a commandline command, and can output a log

    cmd list[string]--> commandline command

    """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    result = stdout.strip().decode('utf-8')
    return result


def sftp(connect_type, host, user, pwd, port):
    """
    Connects to a sftp server

    host --> hostname of the server
    user --> username
    pwd --> password
    """
    if connect_type == "paramiko":
        transport = paramiko.Transport((host, port))
        transport.connect(None, user, pwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp
    elif connect_type == "pysftp":
        sftp = pysftp.Connection(host,username=user, password=pwd)
        return sftp
def get_references(client, fp_to_dir, strip_name):
    '''
    get genome references as a list
    '''
    refs = [ref.replace("_" + strip_name, "") for ref in client.listdir(fp_to_dir + '/'+ strip_name)]
    return refs

def group_files(client, references):
    '''
    makes list of all the input/output files, for amplicon architect only
    results --> GRCh38_AA_results
    bed_files --> bed_files
    bambai --> bwa_bam_grch38
    '''
    # groups of files as a list of list
    # for one element: [results folder, bed_files, bam, bai]
    file_groups = []

    for ref in references:
        result_folder = 'files/turner2017/GRCh38_AA_results/' + ref + '_GRCh38_AA_results'
        bed_file = 'files/turner2017/bed_files/' + ref + '_GRCh38_AA_CNV_SEEDS.bed'
        bam = 'files/turner2017/bwa_bam_grch38/' + ref + ".cs.bam"
        bai = 'files/turner2017/bwa_bam_grch38/' + ref + ".cs.bam.bai"
        file_groups.append([ref, result_folder, bed_file, bam, bai])

    return file_groups

def download_files_and_process(client, group):
    '''
    FOR AA USE ONLY
    1. given some group, download test data into correct destination
    2. process files
    3. logs info rmation
    4. delete test files, keep outputs.

    group list[str]--> a group of input files
    '''
    reference = group[0]
    results_folder = group[1]
    bed = group[2]
    bam = group[3]
    bai = group[4]

    # download data locally
    os.mkdir('tempdata/results/'+reference)
    client.get_d(results_folder, ('tempdata/results/'+reference))
    client.get(bed, 'tempdata/bed/' + reference + "_GRCh38_AA_CNV_SEEDS.bed")
    client.get(bam, 'tempdata/bambai/' + reference + ".cs.bam")
    client.get(bai, 'tempdata/bambai/' + reference + "cs.bam.bai")

    result_bed = 'tempdata/bed/' + reference + "_GRCh38_AA_CNV_SEEDS.bed"
    result_bam = 'tempdata/bambai/' + reference + ".cs.bam"
    result_bai = 'tempdata/bambai/' + reference + "cs.bam.bai"

    os.system('python ')
    print("I've done something! ")

    os.remove(result_bed)
    os.remove(result_bam)
    os.remove(result_bai)



if __name__ == "__main__":
    client = sftp('pysftp', "genomequery.ucsd.edu", "sftp_user", "bafnalabsftp", 22)
    references = get_references(client, 'files/turner2017', 'GRCh38_AA_results')
    groups = group_files(client, references)
    download_files_and_process(client, groups[0])



    client.close()
