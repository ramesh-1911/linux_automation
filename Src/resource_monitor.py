import platform
import subprocess

def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

print("Resource Monitoring Report")
print("--------------------------")

if platform.system() == "Windows":
    print("\nDisk Information:")
    print(run_command("wmic logicaldisk get size,freespace,caption"))

    print("\nMemory Information:")
    print(run_command("systeminfo | find \"Total Physical Memory\""))

else:
    print("\nDisk Information:")
    print(run_command("df -h"))

    print("\nMemory Information:")
    print(run_command("free -h"))
