from os import system
def ping(Host):
    """
    Returns True if Host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c "
    args = "ping " + " " + ping_str + " " + Host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args) == 0

# test call
resultado = ping("192.168.195.251")
system("cls")
if resultado == True:
    print("TEM INTERNET")
else:
    print("NÃO TEM INTERNET")
