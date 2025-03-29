# [ URL / Domain Modules ] Example

import os
import sys

class Example :
    """
    IN : 
    OUT : 
    """
    def __init__(self, input_url) :
        self.input_url = input_url
    
    """
    IN : URL
    OUT : Scan Result ( True  : Phishing O / False : Phishing X )
    """
    def scan(self) :
        print("Module Start.")

        # ( ... )

        print("\nModule End.")

# Module Main
if __name__ == "__main__" :
    # Input : URL
    if len(sys.argv) != 2 :
        print("How to Use : python3 example.py < URL >")
        sys.exit(1)
    
    input_url = sys.argv[1]
    example = Example(input_url)
    example.scan()
