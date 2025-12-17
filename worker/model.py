from PIL import Image

def generate(image_path: str, prompt: str):
    # 1. 이미지 로드
    image = Image.open(image_path).convert("RGB")

    # 2. 여기서 실제 모델 호출
    # result = diffusion(image, prompt)
    
    # 지금은 더미
    return {
        "text": f"processed image with prompt: {prompt}",
        "image_path": image_path
    }
