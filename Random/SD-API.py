import requests

def get_stable_diffusion_image(prompt, api_key):
    url = 'https://stablediffusionapi.com/api/v3/text2img'  # Replace with the actual API endpoint
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        # Add any additional data required by the API, e.g., settings, options, etc.
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        # Assuming the API returns the image URL in the response
        image_url = response.json().get('image_url')
        return image_url
    else:
        print(f"Failed to get the image. Status code: {response.status_code}")
        return None

def main():
    prompt = input("Enter your prompt: ")
    api_key = 'DB5QBvN5UtkhzkMG0m77hIHX4BG3wQTGEeEM171wdGInvmbXLHPhsLTRaYuC'  # Replace with your actual API key

    image_url = get_stable_diffusion_image(prompt, api_key)

    if image_url:
        print(f"Image generated. You can view it here: {image_url}")
    else:
        print("Image generation failed.")

if __name__ == "__main__":
    main()
