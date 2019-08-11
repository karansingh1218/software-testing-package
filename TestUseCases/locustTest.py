import os
import subprocess

def locust_command_line_run_creator(filepath, API_ENDPOINT):
    
    locustCommand = "locust -f " +filepath+ " --host=" + API_ENDPOINT
    
    return locustCommand


def run_locust_command(locustCommand):
    
    process = subprocess.Popen([locustCommand], shell=True)
    try:
        print('Running in process', process.pid)
        process.wait(timeout=120)
    except subprocess.TimeoutExpired:
        print('Timed out - killing', process.pid)
        process.kill()
    print('Done')
#     locustRun = os.system(locustCommand)
    
    return "Test is running"


# import subprocess
# # ("exec " + cmd, stdout=subprocess.PIPE, shell=True
# try:
#     sub1 = subprocess.Popen([ "exec " +"locust -f LoadTesting/locustfile.py --host=http://afsconnect1.njit.edu:5681"],stdout=subprocess.PIPE, shell=True)
#     sub2 = subprocess.Popen(["bokeh serve"], shell=True)
#     sub3 = subprocess.Popen(["python LoadTesting/plotter.py"], shell=True)
# except subprocess.CalledProcessError:
#     print("Error")
    
# # webbrowser.open('http://127.0.0.1:8089')

# print(sub1.kill())


# import subprocess

# try:
#     sub1 = subprocess.Popen(["locust -f LoadTesting/randomQueryLocust.py --host=http://afsconnect1.njit.edu:5681"], shell=True)
#     sub2 = subprocess.Popen(["bokeh serve"], shell=True)
#     sub3 = subprocess.Popen(["python LoadTesting/plotter.py"], shell=True)
# except subprocess.CalledProcessError:
#     print("Error")
    
# webbrowser.open('http://127.0.0.1:8089')

# import os
# import signal
# import subprocess
# cmd = "locust -f LoadTesting/locustfile.py --host=http://afsconnect1.njit.edu:5681"
# # The os.setsid() is passed in the argument preexec_fn so
# # it's run after the fork() and before  exec() to run the shell.
# pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
#                        shell=True, preexec_fn=os.setsid) 

# os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups