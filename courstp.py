import sys
import os
import csv
from datetime import datetime

def ping_host(host):
    command = os.system(f"ping {host}")
    return command == 0

def log_result(host, status, log_file):
    with open(log_file, 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{timestamp} - {host} - {status}\n")
        
def log_failures(failures, log_file):
    with open(log_file, 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for host in failures:
            file.write(f"{timestamp} - {host} - Inaccessible\n")

def hostscsv(csv_file):
    hosts = []
    with open(csv_file, 'r') as file:
        lecture = csv.reader(file)
        for ligne in lecture:
            if ligne:
                hosts.append(ligne[0])
    return hosts

def main():
    

    csv_file = "csv_file.csv"
    log_file = "ping_results.log"
    failure_log_file = "ping_failures.log"
    hosts = hostscsv(csv_file)
    failures = []

    for host in hosts:
        status = "Accessible" if ping_host(host) else "Inaccessible"
        log_result(host, status, log_file)
        if status == "Inaccessible":
            failures.append(host)
        print(f"L'hôte {host} est {status}.")
        
    if failures:
        log_failures(failures, failure_log_file)

if __name__ == "__main__":
    main()
