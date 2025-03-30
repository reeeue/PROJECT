# [ URL Modules ] Sub Domain

import os
import sys
from urllib.parse import urlparse

"""
IN : URL
OUT : Scan Result ( True  : Phishing O / False : Phishing X )
"""
class Sub_Domain :
    """
    IN : 
    OUT : 
    """
    def __init__(self, input_url) :
        self.input_url = input_url

        # "OK" Domain List
        self.ok_domain_list = [
            "google.com", "paypal.com", "apple.com", "microsoft.com", "naver.com", "kakao.com"
        ]

    """
    IN : 
    OUT : 
    """
    def scan(self) :
        print("Module Start.\n")

        flag = False

        urlparse_result = urlparse(self.input_url)
        hostname = urlparse_result.hostname

        if hostname is None :
            print("[ ERROR ] Can't Get \"Host Name\" from Input URL.")
            print(f">>>> Input URL : {self.input_url}")
            sys.exit(1)
        
        print(f"[ DEBUG ] Host Name : {hostname}")
        
        for ok_domain in self.ok_domain_list :
            if ok_domain in hostname :
                if not hostname.endswith(ok_domain) :
                    print(f"[ ⚠️ Suspicious ] OK Domain : \"{ok_domain}\"")
                    print(f">>>> Input URL : {self.input_url}")
                    return True
                else :
                    print(f"[ ✅ OK ] OK Domain : \"{ok_domain}\"")
                    return False
        
        if flag == False :
            print("To-Do") # To-Do => ( IF ) Data - Not Exist

        print("\nModule End.")

# Module Main
if __name__ == "__main__" :
    # Input : URL
    if len(sys.argv) != 2 :
        print("How to Use : python3 sub_domain.py < URL >")
        sys.exit(1)
    
    input_url = sys.argv[1]
    sub_domain = Sub_Domain(input_url)
    sub_domain.scan()
