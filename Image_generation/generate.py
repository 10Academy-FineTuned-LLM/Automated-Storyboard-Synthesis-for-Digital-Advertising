#import matplotlib.pyplot as plt
from PIL import Image
import auth_token
import torch
from diffusers import DiffusionPipeline
from diffusers.utils import make_image_grid

import numpy as np
from torchvision import transforms
import matplotlib.pyplot as plt
from transformers import pipeline, AutoTokenizer
from compel import Compel, ReturnedEmbeddingsType

seed = 42

#pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", tf_dtypes=torch.float16,use_auth_token=auth_token)
pipeline = DiffusionPipeline.from_pretrained(
  "stabilityai/stable-diffusion-xl-base-1.0",
  variant="fp16",
  use_safetensors=True,
  torch_dtype=torch.float16
).to("cuda")


max_length = pipeline.tokenizer.model_max_length
print(max_length)

from torch import autocast

prompt = ["""Create the Background Animation with a suspenseful animation of a LEGO CITY set, showcasing buildings, vehicles, and mini-figures coming to life in a dynamic, 3D environment.
Position the animation to cover the entire background of the frame (0, 0, 600, 600).
Add the Tagline "YOUR CITY, NO LIMITS" in bold as a text, vibrant letters. Place it horizontally centered and near the top of the frame, within the bounding box (50, 510, 500, 90).
Implement the Countdown Timer as a digital timer with LEGO brick styling. Set it to the bottom-right corner of the frame, within the bounding box (530, 10, 70, 70)."""]
#with autocast("cuda"):
    #output = pipeline(prompt)
#tokenizer = AutoTokenizer.from_pretrained("")


#encode the texts to into embeddings
compel = Compel(
  tokenizer=[pipeline.tokenizer, pipeline.tokenizer_2] ,
  text_encoder=[pipeline.text_encoder, pipeline.text_encoder_2],
  returned_embeddings_type=ReturnedEmbeddingsType.PENULTIMATE_HIDDEN_STATES_NON_NORMALIZED,
  requires_pooled=[False, True]
)
conditioning, pooled = compel(prompt)

# generate image
generator = [torch.Generator().manual_seed(33) for _ in range(len(prompt))]
#images = pipeline(prompt_embeds=conditioning, pooled_prompt_embeds=pooled, generator=generator, num_inference_steps=30).images
#images


with autocast("cuda"):
    output = pipeline(prompt_embeds=conditioning, pooled_prompt_embeds=pooled, generator=generator, num_inference_steps=30)
    
make_image_grid(output.images, rows=1, cols=1)

print(output.images[0])
output.images[0].save("output.png")


