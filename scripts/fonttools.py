"""Google Bard API test"""

import os
import bardapi
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("PSID")

print(bardapi.core.Bard(token).get_answer("Do you know fonttools?")["content"])
print(
    bardapi.core.Bard(token).get_answer(
        "Can you make a fonttools script to set the name table of a font?"
    )["content"]
)
print(
    bardapi.core.Bard(token).get_answer(
        "And how about making the same script but with fontTools for rust?"
    )["content"]
)
