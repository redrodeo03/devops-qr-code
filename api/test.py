import os
from dotenv import load_dotenv
load_dotenv()

print("AWS_ACCESS_KEY:", os.getenv("AWS_ACCESS_KEY"))
print("AWS_SECRET_KEY:", os.getenv("AWS_SECRET_KEY"))