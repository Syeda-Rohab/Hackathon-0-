# AI Employee Foundation - Bronze Tier Submission

## Project Overview
This project implements an AI employee foundation that monitors Gmail, processes important emails, creates action plans, and maintains an Obsidian vault with status updates.

## System Architecture

### Components
1. **Obsidian Vault**: Contains all processed information in markdown format
2. **Gmail Watcher**: Monitors for important emails using OAuth authentication
3. **Claude Processor**: Creates action plans from email content
4. **File Manager**: Organizes files in the three-folder system
5. **Dashboard Updater**: Maintains live status updates

### Folder Structure
- `/Inbox` - Reserved for future use
- `/Needs_Action` - Emails requiring processing and action plans
- `/Done` - Completed tasks and processed emails

### Key Files
- `Dashboard.md` - Live status dashboard
- `Company_Handbook.md` - Rules and skills documentation
- `gmail_auth.py` - Gmail authentication module
- `ai_employee.py` - Main system logic (full version)
- `ai_employee_mock.py` - Simulated version for testing
- `setup.py` - Setup and installation script

## Workflow Process
1. Gmail watcher monitors for important emails
2. Important emails are saved as EMAIL_xxx.md in /Needs_Action
3. Claude processes emails to create PLAN_xxx.md files
4. Processed files are moved to /Done
5. Dashboard is updated with current status

## Setup Instructions

### Prerequisites
- Python 3.6+
- Google Cloud account with Gmail API enabled

### Steps
1. Clone/download this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up Gmail API credentials:
   - Go to Google Cloud Console
   - Create a new project or select existing one
   - Enable Gmail API
   - Create credentials for Desktop Application
   - Download credentials as 'credentials.json'
4. Run the system: `python ai_employee.py`

## Testing
The system has been tested with the mock version (`ai_employee_mock.py`) which simulates the email processing workflow. When run, it creates sample EMAIL_xxx.md and PLAN_xxx.md files, moves them to the Done folder, and updates the dashboard.

## Features Implemented
✅ Obsidian vault with Dashboard.md and Company_Handbook.md
✅ Gmail OAuth setup (credentials handling)
✅ Automated email processing workflow
✅ Three-folder system (Inbox, Needs_Action, Done)
✅ Agent skills for email processing, task planning, status reporting, and document management
✅ Dashboard auto-update functionality
✅ Local Python script with scheduling capability

## Cron Job Setup (Windows)
Use the provided `run_ai_employee.bat` file to schedule the script with Windows Task Scheduler.

## Security Considerations
- OAuth tokens are stored locally in token.pickle
- No passwords are used, only secure OAuth 2.0
- All data is stored locally in the vault

## Future Enhancements
- Integration with Claude API for real AI processing
- More sophisticated email filtering and prioritization
- Enhanced error handling and logging
- Web interface for monitoring