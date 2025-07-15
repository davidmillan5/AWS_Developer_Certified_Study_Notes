import boto3

# Explicit Client Configuration
polly = boto3.client('polly',
                     region_name='us-east-2',
                     aws_access_key_id='YOUR_ACCESS_KEY',
                     aws_secret_access_key='YOUR_SECRET_KEY')

response = polly.synthesize_speech(Text='Hello World!',
                                   OutputFormat='mp3',
                                   VoiceId='Aditi')

# Save the audio from the response
if 'AudioStream' in response:
    with response['AudioStream'] as stream:
        audio = stream.read()
        with open("helloworld.mp3", "wb") as file:
            file.write(audio)
else:
    print("Could not stream audio")


