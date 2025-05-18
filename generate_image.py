from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os


prompt = input("Enter your image description (prompt): ")

# Model config
model_id = "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if torch.cuda.is_available() else torch.float32

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=dtype,
    use_safetensors=True  
).to(device)

# Generate image
with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
    image = pipe(prompt, guidance_scale=7.5, num_inference_steps=30).images[0]

# Save and show
output_file = "output.png"
image.save(output_file)
print(f"✅ Image saved as: {output_file}")
image.show()
