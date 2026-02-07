"""
Setup script for AI Employee Foundation
Installs dependencies and prepares the system
"""

import os
import sys
import subprocess

def install_dependencies():
    """Install required Python packages"""
    print("Installing required packages...")
    
    packages = [
        "google-auth",
        "google-auth-oauthlib", 
        "google-auth-httplib2",
        "google-api-python-client"
    ]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"[SUCCESS] {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"[FAILED] Failed to install {package}")

def create_cron_script():
    """Create a script that can be used with cron/scheduler"""
    cron_script = '''@echo off
cd /d "%~dp0"
python ai_employee.py
'''
    
    with open("run_ai_employee.bat", "w") as f:
        f.write(cron_script)
    
    print("Created run_ai_employee.bat for Windows scheduling")

def create_readme():
    """Create README with setup instructions"""
    readme_content = """# AI Employee Foundation - Bronze Tier

## Setup Instructions

### 1. Gmail API Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Gmail API for the project
4. Create credentials for Desktop Application
5. Download the credentials JSON file as `credentials.json` in this directory

### 2. Install Dependencies
Run the following command to install required packages:
```
pip install -r requirements.txt
```

Or install manually:
```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 3. Run the System
```
python ai_employee.py
```

## System Components

### Folder Structure
- `/Inbox` - Incoming emails (not currently used, but reserved)
- `/Needs_Action` - Emails requiring processing and action plans
- `/Done` - Completed tasks and processed emails

### Files
- `Dashboard.md` - Live status dashboard
- `Company_Handbook.md` - Rules and skills documentation
- `gmail_auth.py` - Gmail authentication module
- `ai_employee.py` - Main system logic

## Workflow
1. Gmail watcher monitors for important emails
2. Important emails are saved as EMAIL_xxx.md in /Needs_Action
3. Claude processes emails to create PLAN_xxx.md files
4. Processed files are moved to /Done
5. Dashboard is updated with current status

## Scheduling
To run continuously, schedule `run_ai_employee.bat` to run at desired intervals.
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print("Created README.md with setup instructions")

def create_requirements():
    """Create requirements.txt file"""
    requirements = """google-auth==2.48.0
google-auth-oauthlib==1.2.4
google-auth-httplib2==0.3.0
google-api-python-client==2.189.0
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements)
    
    print("Created requirements.txt")

def main():
    print("Setting up AI Employee Foundation...")
    
    install_dependencies()
    create_cron_script()
    create_readme()
    create_requirements()
    
    print("\nSetup complete!")
    print("\nNext steps:")
    print("1. Set up Gmail API credentials (see README.md)")
    print("2. Run 'python ai_employee.py' to test the system")

if __name__ == "__main__":
    main()