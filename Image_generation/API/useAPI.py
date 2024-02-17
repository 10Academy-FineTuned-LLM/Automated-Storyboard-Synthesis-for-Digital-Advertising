import requests
import json

url = "https://stablediffusionapi.com/api/v3/inpaint"



payload = json.dumps({
  "key": "",
  "prompt": "a cat sitting on a bench",
  "negative_prompt": None,
  "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",
  "mask_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png",
  "width": "512",
  "height": "512",
  "samples": "1",
  "num_inference_steps": "30",
  "safety_checker": "no",
  "enhance_prompt": "yes",
  "guidance_scale": 7.5,
  "strength": 0.7,
  "base64": "no",
  "seed": None,
  "webhook": None,
  "track_id": None
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)