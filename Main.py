import socket
import subprocess

host = input("website> ")
ip = socket.gethostbyname(host)

def ping(ip_address):
    try:
      output = subprocess.check_output(
            ['ping', '-c', '4', ip_address] if subprocess.os.name != 'nt' else ['ping', '-n', '4', ip_address],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
      print(output)
      return True
    except subprocess.CalledProcessError as e:
        print(f"Ping failed: {e.output}")
    return False

if ping(ip):
    print(f"Ping to {ip} was successful!")
else:
    print(f"Ping to {ip} failed.")
