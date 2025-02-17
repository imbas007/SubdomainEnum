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

## Installation
```sh
sudo apt install jq curl
```
Or install via Homebrew (for macOS):
```sh
brew install jq curl
```
Install other tools from their respective repositories.

## Usage
```sh
python subenum.py example.com
```
Replace `example.com` with your target domain.
