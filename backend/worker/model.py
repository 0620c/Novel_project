from PIL import Image
import torch
from diffusers import StableDiffusionImg2ImgPipeline

# 1. 모델 로드 (파일 import 시 1번만 실행됨)
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")   # CPU면 .to("cpu")

pipe.set_progress_bar_config(disable=True)

# 2. 실제 호출 함수
def generate(image_path: str, prompt: str):
    image = Image.open(image_path).convert("RGB")

    result = pipe(
        prompt=prompt,
        image=image,
        strength=0.7,
        guidance_scale=7.5
    ).images[0]

    # 결과 저장
    output_path = image_path.replace("uploads", "static")
    result.save(output_path)

    return {
        "text": prompt,
        "image_path": output_path
    }
