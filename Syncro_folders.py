import shutil
import time
import logging
import argparse
import os


def sync_folder(source_folder, replica_folder):
    
    logging.basicConfig(filename=args.log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
    
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)
    
    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)
        replica_file_path = os.path.join(replica_folder, filename)

        logging.debug("Copying '{}' from '{}' to '{}'.".format(filename, source_file_path, replica_file_path))

        if os.path.exists(source_file_path):
            if not os.path.exists(replica_file_path):
                if os.path.isfile(source_file_path):
                    shutil.copy(source_file_path, replica_file_path)
                    logging.info("Copied '{}' to replica folder.".format(filename))
                elif os.path.isdir(source_file_path):
                    shutil.copytree(source_file_path, replica_file_path)
                    logging.info("Copied '{}' to replica folder.".format(filename))
        else:
            if os.path.exists(replica_file_path) and not os.path.exists(source_file_path):
                if os.path.isfile(replica_file_path):
                    os.remove(replica_file_path)
                    logging.info("Deleted '{}' from replica folder.".format(filename))
                elif os.path.isdir(replica_file_path):
                    shutil.rmtree(replica_file_path)
                    logging.info("Deleted '{}' from replica folder.".format(filename))

parser = argparse.ArgumentParser(description="Folder Synchronization Program")
parser.add_argument("source_folder", help="/Users/amine/Documents/Syncro_Program/source_folder")
parser.add_argument("replica_folder", help="/Users/amine/Documents/Syncro_Program/replica_folder")
parser.add_argument("--log_file", default="sync.log", help="")
args = parser.parse_args()

#source_folder = ""
#replica_folder = "/Users/amine/Documents/Syncro_Program/replica_folder"
sync_folder(args.source_folder, args.replica_folder)
