# Linux-Scripts
Hello, World! Includes Shell and Pyhton scripts written by me which can help a lot. More details in README. 


## time_setter

**Contains time.py**


I created this command for setting accurate time in linux system. Usually while dual booting, either windows time messes up or linux time gets messed up. 

So, simply execute this script during startup and it will get time according to IP address(requires internet), and set it up.

add exec ~/path_to_script in init in any linux systems.

Make sure to give executable rights to this script. Also this requires root permission, in order to do so, type as su **EDITOR=vim visudo** and add the following line:
> *user_name* ALL=NOPASSWD: ALL

This much should do!
