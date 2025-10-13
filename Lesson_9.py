import logging

logging.basicConfig(
    filename = "trace.log",
    filemode = "w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    print(f"{300*700}")
except Exception as e:
    logging.exception("Щось не так")
    