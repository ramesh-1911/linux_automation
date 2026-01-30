import logging
import platform

# Configure logging
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Automation script started")

os_name = platform.system()
logging.info(f"Operating System detected: {os_name}")

if os_name == "Windows":
    logging.info("Running Windows specific tasks")
else:
    logging.info("Running Linux specific tasks")

logging.info("Automation script finished successfully")
