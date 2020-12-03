# -*- coding: utf-8 -*-
"""Bootstrap file."""

from src import *

def main():
    # Creating schema and tables:
    create_tables.main()

    # Running ETL pipeline:
    etl.main()
    
    
if __name__=="__main__":
    main()