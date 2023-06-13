"""Google Bard API test"""

import os
import bardapi
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("PSID")

response = bardapi.core.Bard(token).get_answer("Are you Bard?")["content"]
print(response)
