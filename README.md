# berachain_checker

### Donation ``` TRC20 - TRWzXZE16bgJg3eHa9n8q4ioZjMgKHwF9a ```
<img src="usdt.jpg" alt="Donation" width="150"/>

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DenisHumen/berachain_checker.git
    cd berachain_checker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Prepare the `walletss.txt` file with wallet addresses, one per line.

2. Prepare the `proxy.txt` file with proxy addresses, one per line.

3. Run the script:
    ```sh
    python main.py
    ```

4. The results will be saved in `result.csv` in the format `address,value`.

## Example

Example content of `walletss.txt`:
```
0xD360715608c026ec62d265Cfe4d3453453453451
0x15fA602B8F6345345345345345fghfghfghf5855
```

Example content of `proxy.txt`:
```
http://proxy1.example.com:8080
http://proxy2.example.com:8080
```

## Donation

If you find this project useful, consider donating:

TRC-20: `TRWzXZE16bgJg3eHa9n8q4ioZjMgKHwF9a`

## Author

Denis Humen

[https://github.com/DenisHumen](https://github.com/DenisHumen)