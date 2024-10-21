Overview:
This project implements an Ansible-based automation framework to deploy and manage a Python keylogger on remote Windows machines. The system allows the deployment, execution, and management of the keylogger 
through scheduled tasks on the target machine. It also enables the printing of captured keystrokes to the control machine. The architecture uses Ansible to scripts and their tasks, 
providing a streamlined way to deploy and execute keylogging activities remotely.

Features:
  Remote Keylogger Deployment: Automatically deploy the Python keylogger to target Windows machines.
  Log Retrieval: Fetch the keylogger's output log from the remote Windows machine for analysis.
  File Removal: Delete the keylogger files from the target after execution.
  Popups: Send messages alerting the target that they are being watched and how keystrokes have been logged.
  Spooky Sound: When the letter "s" is pressed, a sound is made on the machine. (This worked well on my host machine but had to be commented out to be fixed later because it did not offer the same results on the target).

Installation (more information is released in the "Setup Instructions" file)

Prerequisites:
  Ansible: Installed on the control node.
  Python3: Installed on both the control node and Windows machine (Python 3.12 on Windows).
  Windows Machine: Configured to accept Ansible commands (via WinRM).

Steps:
  Clone the repository on the Ansible control node.
  Prepare the keylogger.py file and ensure it is accessible on the control node.
  Set up the Ansible inventory file with the details of the target Windows machines.
  Run the ansible-playbook to deploy and manage the keylogger on the target machine.

Usage:
  Deploy the Keylogger:
    Run the main_playbook.yml playbook to install necessary dependencies, copy the keylogger script to the remote Windows machine, and schedule the keylogger task.

Flaws: 
  A python exe appears on the target machine which could easily be closed, stopping the program (need to hide the window pop up in the future)
  The keylogger program only ends when the "esc" key is pressed. This is good for continuous information gathering however, the feedback is not scheduled to appear on the control machine until the program has finished. 
  (Would like feedback throughout the duration of the program if possible).
