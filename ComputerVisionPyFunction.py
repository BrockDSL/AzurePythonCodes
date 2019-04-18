print("I am running doobly doo!!!")

def img_analysis():
    import requests
    import matplotlib.pyplot as plt
    import json
    from PIL import Image
    from io import BytesIO
    
    subscription_key = "756a34329ff1430799aee933df7b91b8"
    assert subscription_key
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
    # You have use the same region from your subscription key in the above address
    analyze_url = vision_base_url + "analyze"
    
    image_url = input("Paste an image URL here :")
    
    headers = {'Ocp-Apim-Subscription-Key': subscription_key }
    params  = {'visualFeatures': 'Categories,Description,Color'}
    data    = {'url': image_url}
    response = requests.post(analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    
    #The code below prints out the JSON stuff so you can see what gets returned 
    #and makes up a caption based on the keywords that the tool finds
    analysis = response.json()
    print(json.dumps(response.json()))
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    
    # Display the image and the above mentioned caption.
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(image_caption, size="x-large", y=-0.1)
    plt.show()

def img_analysis_flex(image_urlish):
    import requests
    import matplotlib.pyplot as plt
    import json
    from PIL import Image
    from io import BytesIO
    
    subscription_key = "756a34329ff1430799aee933df7b91b8"
    assert subscription_key
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
    # You have use the same region from your subscription key in the above address
    analyze_url = vision_base_url + "analyze"
    
    image_url = image_urlish
    
    headers = {'Ocp-Apim-Subscription-Key': subscription_key }
    params  = {'visualFeatures': 'Categories,Description,Color'}
    data    = {'url': image_url}
    response = requests.post(analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    
    #The code below prints out the JSON stuff so you can see what gets returned 
    #and makes up a caption based on the keywords that the tool finds
    analysis = response.json()
    print(json.dumps(response.json()))
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    
    # Display the image and the above mentioned caption.
    image = Image.open(BytesIO(requests.get(image_url).content))
    plt.imshow(image)
    plt.axis("off")
    _ = plt.title(image_caption, size="x-large", y=-0.1)
    plt.show()

img_analysis()