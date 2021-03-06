# Automate Edfa3ly Cart

This task for automating Edfa3ly cart using BDD technique (Behaviour Driven Development) to autmate the below scenarios.

* Automated product link
* Nonautomated product link
* Prohibted product link

This task implemented and tested on Ubuntu 18.04 using
* Python3
* Selenium webdriver
* Behave framework


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages in the requirements.txt.

```bash
pip3 install -r requirements.txt
```

## Usage

## Running feature files
From `edfa3ly-tech-task` root directory run the following commands.
```bash
behave features/prohibited_product/features
behave features/automated_product/features
behave features/non_automated_product/features
```

## Bug reporting
Issues found while testing reported in the repo [issues](https://github.com/unxusr/edfa3ly/issues)
