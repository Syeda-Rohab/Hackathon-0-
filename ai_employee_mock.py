"""
Simplified AI Employee Foundation - Mock Version
This version simulates the workflow without requiring full Gmail API access
"""

import os
import json
import time
from datetime import datetime

# Define folder paths
VAULT_PATH = "bronze_vault"
INBOX_PATH = os.path.join(VAULT_PATH, "Inbox")
NEEDS_ACTION_PATH = os.path.join(VAULT_PATH, "Needs_Action")
DONE_PATH = os.path.join(VAULT_PATH, "Done")
DASHBOARD_FILE = os.path.join(VAULT_PATH, "Dashboard.md")

class AIEmployee:
    def __init__(self):
        self.last_checked_time = None
        
    def setup_directories(self):
        """Create required directories if they don't exist"""
        os.makedirs(INBOX_PATH, exist_ok=True)
        os.makedirs(NEEDS_ACTION_PATH, exist_ok=True)
        os.makedirs(DONE_PATH, exist_ok=True)
        
    def simulate_get_emails(self, max_results=3):
        """Simulate getting emails (since we can't access Gmail API directly)"""
        print("Simulating email retrieval...")
        
        # Create mock emails
        mock_emails = [
            {
                'id': 'mock1',
                'subject': 'Quarterly Budget Review Required',
                'sender': 'boss@company.com',
                'body': 'Please review and approve the quarterly budget by end of week.',
                'timestamp': datetime.now().isoformat()
            },
            {
                'id': 'mock2',
                'subject': 'Team Meeting Tomorrow',
                'sender': 'hr@company.com',
                'body': 'Reminder about the team meeting tomorrow at 10 AM in conference room.',
                'timestamp': datetime.now().isoformat()
            },
            {
                'id': 'mock3',
                'subject': 'Project Deadline Update',
                'sender': 'manager@company.com',
                'body': 'The project deadline has been moved to next Friday. Please adjust your plans accordingly.',
                'timestamp': datetime.now().isoformat()
            }
        ]
        
        return mock_emails[:max_results]
    
    def create_email_note(self, email):
        """Create an EMAIL_xxx.md file in Needs_Action folder"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")  # Include microseconds for uniqueness
        filename = f"EMAIL_{timestamp}.md"
        filepath = os.path.join(NEEDS_ACTION_PATH, filename)
        
        content = f"""# Email Note: {email['subject']}

## Sender
{email['sender']}

## Date
{email['timestamp']}

## Content
{email['body']}

## Action Required
- [ ] Review and prioritize
- [ ] Create action plan if needed
- [ ] Process and move to Done

## Priority
- [ ] High
- [ ] Medium  
- [ ] Low
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created email note: {filename}")
        return filepath
    
    def process_with_claude(self, email_note_path):
        """Simulate processing with Claude to create PLAN_xxx.md"""
        # In a real implementation, this would call the Claude API
        # For now, we'll simulate the process
        
        with open(email_note_path, 'r', encoding='utf-8') as f:
            email_content = f.read()
        
        # Extract subject from the email note
        subject_line = email_content.split('\n')[0]  # "# Email Note: Subject"
        subject = subject_line.replace("# Email Note: ", "").strip()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")  # Include microseconds for uniqueness
        filename = f"PLAN_{timestamp}.md"
        filepath = os.path.join(NEEDS_ACTION_PATH, filename)
        
        # Simulated plan content
        plan_content = f"""# Action Plan: {subject}

## Summary
This plan was generated based on the email titled "{subject}".

## Tasks
1. [ ] Task 1 - Description of first action item
2. [ ] Task 2 - Description of second action item
3. [ ] Task 3 - Description of third action item

## Timeline
- Priority: Medium
- Due Date: Within 24-48 hours

## Resources Needed
- Access to relevant documents
- Team member consultation if required

## Dependencies
- Previous related tasks completion
- Availability of required resources

## Success Criteria
- [ ] All action items completed
- [ ] Stakeholders notified of completion
- [ ] Follow-up scheduled if needed
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(plan_content)
        
        print(f"Created action plan: {filename}")
        return filepath
    
    def move_to_done(self, file_path):
        """Move processed file to Done folder"""
        filename = os.path.basename(file_path)
        new_path = os.path.join(DONE_PATH, filename)
        
        # Move the file
        os.rename(file_path, new_path)
        print(f"Moved to Done: {filename}")
        return new_path
    
    def update_dashboard(self):
        """Update Dashboard.md with current status"""
        # Count files in each folder
        inbox_count = len([f for f in os.listdir(INBOX_PATH) if f.endswith('.md')])
        needs_action_count = len([f for f in os.listdir(NEEDS_ACTION_PATH) if f.endswith('.md')])
        done_count = len([f for f in os.listdir(DONE_PATH) if f.endswith('.md')])
        
        # Read existing dashboard content
        if os.path.exists(DASHBOARD_FILE):
            with open(DASHBOARD_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        else:
            lines = []
        
        # Find and update the status section
        new_lines = []
        in_status_section = False
        
        for line in lines:
            if line.strip() == "## Status Overview":
                new_lines.append(line)
                new_lines.append(f"- **Active Tasks**: {needs_action_count}\n")
                new_lines.append(f"- **Completed Tasks**: {done_count}\n")
                new_lines.append("- **System Status**: Active\n")
                new_lines.append(f"- **Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                in_status_section = True
            elif in_status_section and line.startswith("-"):
                # Skip old status lines
                continue
            elif in_status_section and line.startswith("##"):
                # End of status section, add the line and reset flag
                new_lines.append(line)
                in_status_section = False
            else:
                new_lines.append(line)
        
        # Write updated content back to dashboard
        with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print("Dashboard updated!")
    
    def run_cycle(self):
        """Run one complete cycle of the AI employee workflow"""
        print("\n=== Starting AI Employee Cycle ===")
        
        # Get simulated emails
        emails = self.simulate_get_emails(max_results=3)
        print(f"Found {len(emails)} simulated emails")
        
        # Process each email
        for email in emails:
            print(f"Processing: {email['subject']}")
            
            # Create email note in Needs_Action folder
            email_note_path = self.create_email_note(email)
            
            # Process with Claude to create plan
            plan_path = self.process_with_claude(email_note_path)
            
            # Move both files to Done folder
            self.move_to_done(email_note_path)
            self.move_to_done(plan_path)
        
        # Update dashboard
        self.update_dashboard()
        
        print("=== Cycle Complete ===\n")
    
    def start_monitoring(self, interval_minutes=30):
        """Start continuous monitoring (simulated)"""
        print(f"Starting simulated monitoring (checking every {interval_minutes} minutes)")
        
        while True:
            try:
                self.run_cycle()
                print(f"Sleeping for {interval_minutes} minutes...")
                time.sleep(interval_minutes * 60)
            except KeyboardInterrupt:
                print("\nMonitoring stopped by user.")
                break
            except Exception as e:
                print(f"Error during monitoring cycle: {e}")
                print("Retrying in 5 minutes...")
                time.sleep(5 * 60)

def main():
    ai_employee = AIEmployee()
    
    # Setup directories
    ai_employee.setup_directories()
    
    # Run one cycle for testing
    ai_employee.run_cycle()
    
    print("System is ready! To run continuously, uncomment the monitoring line in the main function.")

if __name__ == "__main__":
    main()