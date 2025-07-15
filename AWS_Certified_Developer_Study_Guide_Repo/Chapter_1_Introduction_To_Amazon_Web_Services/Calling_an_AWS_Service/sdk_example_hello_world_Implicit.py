import boto3

# Create a session using the 'developer' profile
session = boto3.Session(profile_name='developer', region_name='us-east-2')

# Create a Polly client from that session
polly = session.client('polly')

response = polly.synthesize_speech(Text='Success is not final, failure is not fatal: It is the courage to continue that counts.',
                                   OutputFormat='mp3',
                                   VoiceId='Aditi')

# Save the audio from the response
if 'AudioStream' in response:
    with response['AudioStream'] as stream:
        audio = stream.read()
        with open("quote.mp3", "wb") as file:
            file.write(audio)
else:
    print("Could not stream audio")
