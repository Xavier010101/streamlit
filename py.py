
import runpod
import os
from dotenv import load_dotenv

load_dotenv()

runpod.api_key = os.getenv("runpod")  # you can find this in settings

endpoint = runpod.Endpoint("vyd0wqd6ci6tyf")

run_request = endpoint.run(
    {"prompt": "how are you ? Please tell me about usa and their history"}
)


print(run_request.output())
