# application_resource_monitor
Application Resource Monitor

Contents

•	Introduction

•	Code Submission

•	Technical Documentation

1.	Purpose
2.	Functionality
3.	Usage
4.	Dependencies
5.	Execution
6.	Limitations
   
•	Assessment Criteria

•	Contact Information


Introduction

This code submission contains a Python script that monitors CPU usage of a specified application using the psutil library. The script prompts the user for the application name and continuously displays the CPU usage percentage. 

Code Submission

The code has been submitted as a compressed zip file named application_resource_monitor.zip. The zip file contains the following files:

•	monitor_resource_usage.py: The Python script for monitoring CPU usage.

•	README.md: The technical documentation explaining the code.

Technical Documentation

1. Purpose
   
The purpose of this code is to provide a simple way to monitor CPU usage of a specific application. It uses the psutil library to gather CPU usage information and prompts the user for the application name. The script is designed for educational purposes and showcases basic use of the psutil library.

2. Functionality
   
The code monitors CPU usage of a user-specified application in real-time. It continuously displays the CPU usage percentage at regular intervals.

3. Usage

   
   

 A.	Unzip the application_resource_monitor.zip file.
 
 B.	Open a terminal or command prompt.
 
 C.	Navigate to the directory where the script is located.
 
 D.	Run the script using the command: python3 monitor_resource_usage.py.
 
 E.	Enter the name of the application you want to monitor when prompted.
 

4. Dependencies
   
The script requires the psutil library, which can be installed using pip:

Copy code

pip install psutil

5. Execution
   
The script starts by prompting the user for the application name. It then continuously monitors the CPU usage of the specified application and displays the CPU usage percentage at regular intervals.


6. Limitations
   
The code only monitors CPU usage and GPU usage.
The code assumes that the specified application is running when monitoring begins.
GPU usage monitoring is not implemented due to the lack of a generic library for all GPUs.

Contact Information

For any questions or clarifications, please contact Himanshu Sonkar at himanshusonkar373@gmail.com































