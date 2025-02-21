# GetFromBSE
This script pulls a basis set from the [Basis Set Exchange](https://www.basissetexchange.org/) (BSE) and saves it to a file.

## Requirements
Install the `basis_set_exchange` library using pip (if you haven't already):
```sh
pip install basis_set_exchange
```

## Usage
```sh
python getfrombse.py [-h] basis_set [format] [extension]
```

### Arguments
- `basis_set` (str): The name of the basis set to pull.
- `format` (str, optional): The format to save the basis set in. Default is `gaussian94`.
- `extension` (str, optional): The extension to save the basis set in. Default is the same as the format.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
