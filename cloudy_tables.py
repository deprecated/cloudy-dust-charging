from astropy.table import Table
import glob
import os

# File extensions that might be present, which are NOT Cloudy save files
IGNORE_EXTS = ["pdf", "png", "jpg"]

class CloudyModel(object):
    """Lightweight wrapper for output from Cloudy run 

    `data` contains dict of astropy.Table's, one for each save file 
    """
    def __init__(self, prefix, dir="."):
        self.files = glob.glob(os.path.join(dir, prefix) + ".*")
        self.data = {}
        self.io = {}
        for file_ in self.files:
            print(f"Trying to read from {file_}")
            saveid = file_.split(os.path.extsep)[-1]
            if saveid in IGNORE_EXTS:
                # Figure files, etc need to be skipped
                pass
            elif saveid in ["in", "out"]:
                # Special case of input and output files
                with open(file_) as f:
                    # Just save the whole file as a string
                    self.io[saveid] = f.read()
            else:
                # Assume all else are save files
                try:
                    print(f"Reading data table from {saveid}")
                    self.data[saveid] = Table.read(
                        file_, format="ascii.commented_header", delimiter="\t")
                    print(f"Success with {saveid}")
                except UnicodeDecodeError:
                    # Assume this is not a Cloudy file
                    pass
