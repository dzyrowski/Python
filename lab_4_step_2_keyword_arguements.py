import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 
    
kwargs={
    "Text": "I am learing to code in AWS",
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "es"
}

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()

