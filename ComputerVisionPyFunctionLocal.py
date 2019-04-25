print("I am working!!")

def image_analysis_local(image_path, subscription_key):
    import requests
    import matplotlib.pyplot as plt
    from PIL import Image
    from io import BytesIO
    
    # Input valid subscription key.
    #subscription_key = input("Enter your API key")
    assert subscription_key
    
    # You have use the same region from your subscription key in the above address
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
    analyze_url = vision_base_url + "analyze"
    
    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params     = {'visualFeatures': 'Categories,Description,Color'}
    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    
    #The code below prints out the JSON stuff so you can see what gets returned 
    #and makes up a caption based on the keywords that the tool finds
    analysis = response.json()
    print(analysis)
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    
    # Display the image and the above mentioned caption.
    image = Image.open(BytesIO(image_data))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(image_caption, size="x-large", y=-0.1)
    plt.show()


pics = ("LIST OF IMAGES TO ANALYSE")


for pic in pics:
    image_analysis_local(pic,"Your API Key Here")

