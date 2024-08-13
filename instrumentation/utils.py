import requests

def upload_image_to_supabase(image_file):

    supabase_url = "https://gbblasxmcvumfinbunbe.supabase.co/storage/v1/s3"
    supabase_bucket = "INFRASTRUCTURES" 
    supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdiYmxhc3htY3Z1bWZpbmJ1bmJlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyMzIyNTAzMywiZXhwIjoyMDM4ODAxMDMzfQ.EACO2V-UT_g8CPqelGunFTBhhDiNhn0OOyyy0Misil8"  # Replace with your Supabase API key

    headers = {
        "apikey": supabase_api_key,
        "Authorization": f"Bearer {supabase_api_key}",
    }

    upload_url = f"{supabase_url}/{supabase_bucket}/{image_file.name}"

    response = requests.put(upload_url, headers=headers, files={'file': image_file})

    if response.status_code == 200:
        image_url = f"https://gbblasxmcvumfinbunbe.supabase.co/storage/v1/object/public/{supabase_bucket}/{image_file.name}"
        return image_url
    else:
        print("Error uploading file:", response.text)
        return None
