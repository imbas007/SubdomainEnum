import os
import subprocess
import argparse

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running command: {command}\n{e}")
        return ""

def save_to_file(filepath, data):
    with open(filepath, "w") as f:
        f.write(data)

def main(domain):
    # Create a directory for the domain
    os.makedirs(domain, exist_ok=True)
    
    # Define output file paths
    crtsh_output = os.path.join(domain, "crtsh.txt")
    subfinder_output = os.path.join(domain, "subfinder.txt")
    findomain_output = os.path.join(domain, "findomain.txt")
    assetfinder_output = os.path.join(domain, "assetfinder.txt")
    final_output = os.path.join(domain, "final.txt")
    clean_sub_output = os.path.join(domain, "clean_sub.txt")
    
    print("[+] Enumerating subdomains...")
    
    # crt.sh enumeration
    print("[*] Running crt.sh...")
    crtsh_cmd = f'curl -s "https://crt.sh/?q=%25.{domain}&output=json" | jq -r ".[].name_value" | sed "s/\\*\\.//g" | sort -u'
    crtsh_result = run_command(crtsh_cmd)
    save_to_file(crtsh_output, crtsh_result)
    
    # subfinder enumeration
    print("[*] Running subfinder...")
    run_command(f'subfinder -d {domain} -silent -all -o {subfinder_output}')
    
    # findomain enumeration
    print("[*] Running findomain...")
    run_command(f'findomain -t {domain} -q > {findomain_output}')
    
    # assetfinder enumeration
    print("[*] Running assetfinder...")
    run_command(f'assetfinder --subs-only {domain} > {assetfinder_output}')
    
    # Combine all results and remove duplicates
    print("[*] Combining results...")
    run_command(f'cat {crtsh_output} {subfinder_output} {findomain_output} {assetfinder_output} | sort -u > {final_output}')
    
    # Run httpx for live subdomain checking
    print("[*] Running httpx...")
    run_command(f'httpx -l {final_output} -silent -o {clean_sub_output}')
    
    print("[+] Subdomain enumeration completed. Results saved in:")
    print(f"    - {crtsh_output}")
    print(f"    - {subfinder_output}")
    print(f"    - {findomain_output}")
    print(f"    - {assetfinder_output}")
    print(f"    - {final_output}")
    print(f"    - {clean_sub_output} (Live subdomains)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Script")
    parser.add_argument("domain", help="Target domain for enumeration")
    args = parser.parse_args()
    main(args.domain)
