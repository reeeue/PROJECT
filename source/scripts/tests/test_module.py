# [ TEST ] Module

import csv
from urllib.parse import urlparse

"""
Get URL Data from "openphish_feed.txt" ( Data File )
"""
def get_url_data(file_path) :
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

"""
Scan with Module
"""
def scan(module_class, data_file_path, result_csv="test_module_result.csv") :    
    urls = get_url_data(data_file_path)

    print(f"\nNumber of URLs to TEST: {len(urls)}\n")

    results = []

    for index, url in enumerate(urls, 1) :
        print(f"[ + ] [{index:04d}] {url}")

        try :
            module_instance = module_class(url)
            is_suspicious = module_instance.scan()  # Return Value : True / False
        except Exception as e :
            print(f"[ ERROR ] ? : {e}") # Keep Loop
            is_suspicious = False  # To-Do

        if is_suspicious :
            result = "Suspicious"
        else :
            result = "OK"

        hostname = urlparse(url).hostname or ""

        results.append({
            "result": result,
            "url": url,
            "hostname": hostname
        })

        print(f"[ Result ] {result}")
        print("-" * 60)

    with open(result_csv, mode="w", newline='', encoding="utf-8") as f :
        writer = csv.DictWriter(f, fieldnames=["result", "url", "hostname"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSuccess of \"TEST\" => {result_csv}\n")

"""
Main
"""
if __name__ == "__main__" :
    from url_homograph import Homograph # Example : Url Modules - "url_homograph.py" ( Homograph )
    
    data_file_path = "openphish_feed.txt"
    scan(Homograph, data_file_path)
