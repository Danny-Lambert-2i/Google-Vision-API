import os 

def detect_logos(path):
    """Detects logos in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    file_name = os.path.abspath(path)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

# # Premier League Badges
# detect_logos('./images/pl.jpg')
# Man united old logos
detect_logos('./images/manutd.jpg')
# Leeds test logo 
# detect_logos('./images/leeds2.jpg')
# # Leeds test logo 2
# detect_logos('./images/leeds.png')
# # Liverpool old Badges
# detect_logos('./images/liverpool.jpg')
# # Detect NFL badges
# detect_logos('./images/nfl.jpg')