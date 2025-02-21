#!/usr/bin/env python

import sys
import argparse
import basis_set_exchange as bse

def pull_from_bse(basis_set:str, format:str, extension:str=None) -> int:
    """
    Pulls a basis set from the Basis Set Exchange (BSE) and saves it to a file.
    Args:
        basis_set (str): The name of the basis set to pull.
        format (str): The format to save the basis set in.
    """
    # grab the list of available formats
    bse_formats = bse.get_formats()
    if format not in bse_formats:
        raise Exception(f"Format {format} not available. Available formats are {bse_formats}")
    
    # pull the basis set
    basis = bse.get_basis(basis_set, fmt=format)
    
    ext = extension or format
        
    filename = f"{basis_set}.{ext}"
    with open(filename, 'w') as f:
        f.write(basis)
        f.close()
    print(f"Basis set {basis_set} saved to {filename}")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Pull a basis set from the Basis Set Exchange (BSE) and save it to a file.")
    parser.add_argument("basis_set", type=str, help="The name of the basis set to pull.")
    parser.add_argument("format", type=str, nargs='?', default="gaussian94", help="The format to save the basis set in (default: gaussian94).")
    parser.add_argument("extension", type=str, nargs='?', help="The extension to save the basis set in (default: same as format)")
    
    args = parser.parse_args()
    
    print("Basis: ", args.basis_set)
    print("Format: ", args.format)
    print("Extension: ", args.extension)
    
    pull_from_bse(args.basis_set, args.format, args.extension)
    return 0

if __name__ == "__main__":
    main()
