# [ URL Modules ] Sub Domain

import os
import sys
import tldextract
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

        # To-Do
        # "OK" Domain List
        self.ok_domain_list = [
            "google.com", "paypal.com", "apple.com", "microsoft.com", "naver.com", "kakao.com"
        ]
        # To-Do
        # "OK" Keyword List
        self.ok_keyword_list = [
            "google", "paypal", "apple", "microsoft", "naver", "kakao"
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

        extract = tldextract.extract(hostname)
        subdomain = extract.subdomain
        domain = extract.domain
        suffix = extract.suffix
        input_url_domain = f"{domain}.{suffix}"

        print(f"[ DEBUG ] Sub Domain : {subdomain}")
        print(f"[ DEBUG ] Domain : {domain}")
        print(f"[ DEBUG ] Suffix : {suffix}")
        print(f"[ DEBUG ] URL Domain : {input_url_domain}")

        # 1. Not Exist in "OK Domain List"
        if input_url_domain not in self.ok_domain_list :
            suspicious = False

            for keyword in self.ok_keyword_list :
                # 2-1. But Exist in "OK Keyword List" => Suspicious
                if keyword in hostname :
                    print(f"[ ⚠️ Suspicious ]")
                    print(f">>>> ( Suspicious ) Keyword : \"{keyword}\"")
                    print(f">>>> Input URL : {self.input_url}")
                    return True
            
            # 2-2. Not Exist in "OK Keyword List" => OK
            if suspicious == False :
                print(f"[ ✅ OK ]")
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
