# Subdomain Enumeration Tool

This script automates subdomain enumeration using multiple tools, stores results in a domain-specific folder, and filters live subdomains with `httpx`.

## Features
- Fetch subdomains from `crt.sh`
- Use `subfinder`, `findomain`, and `assetfinder` for enumeration
- Combine results and remove duplicates
- Check live subdomains using `httpx`

## Prerequisites
Ensure you have the following tools installed:
- `curl`
- `jq`
- `subfinder`
- `findomain`
- `assetfinder`
- `httpx`

## Usage
Run the script with a domain name as an argument:
```sh
python3 subenum.py domain.com
```

### Example Output
```sh
[+] Enumerating subdomains...
[*] Running crt.sh...
[*] Running subfinder...
[*] Running findomain...
[*] Running assetfinder...
[*] Combining results...
[*] Running httpx...
[+] Subdomain enumeration completed. Results saved in:
    - domain.com/crtsh.txt
    - domain.com/subfinder.txt
    - domain.com/findomain.txt
    - domain.com/assetfinder.txt
    - domain.com/final.txt
    - domain.com/clean_sub.txt (Live subdomains)
```
